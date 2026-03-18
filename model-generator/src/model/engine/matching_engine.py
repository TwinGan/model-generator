from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Any, Callable, Protocol
import uuid

from src.model.engine.orderbook import (
    Order,
    OrderType,
    TimeInForce,
    OrderStatus,
    ExecType,
    Side,
    Session,
    BookType,
    InstrumentOrderBook,
    OrderBookStore,
)


class InstrumentType(str, Enum):
    OPTION = "OPTION"
    FUTURE = "FUTURE"


@dataclass(frozen=True)
class Trade:
    trade_id: str
    order_id: str
    internal_id: str
    symbol: str
    security_id: str
    side: Side
    price: Decimal
    quantity: int
    counterparty_order_id: str
    counterparty_internal_id: str
    counterparty_price: Decimal
    exec_time: str


@dataclass
class TradeReversal:
    reversal_id: str
    original_trade_id: str
    symbol: str
    side: Side
    price: Decimal
    quantity: int
    reason: str
    exec_time: str


@dataclass
class TradeCorrection:
    correction_id: str
    original_trade_id: str
    symbol: str
    side: Side
    new_price: Decimal
    new_quantity: int
    reason: str
    exec_time: str


@dataclass
class OrderValidationResult:
    is_valid: bool
    reject_reason: str | None = None


class PriceValidator(Protocol):
    def __call__(self, order: Order, book: InstrumentOrderBook | None) -> bool: ...


class MatchingEngine:
    def __init__(
        self,
        order_store: OrderBookStore,
        price_validator: PriceValidator | None = None,
        session: Session = Session.OPEN,
    ):
        self.order_store = order_store
        self.price_validator = price_validator or (lambda order, book: True)
        self.session = session
        self.trades: list[Trade] = []
        self.reversals: list[TradeReversal] = []
        self.corrections: list[TradeCorrection] = []
        self._sequence = 0

    def _next_sequence(self) -> int:
        self._sequence += 1
        return self._sequence

    def _get_or_create_book(self, symbol: str, security_id: str) -> InstrumentOrderBook:
        book = self.order_store.get_book(symbol)
        if book is None:
            book = self.order_store.add_book(symbol, security_id)
        return book

    def _check_session(self, order: Order) -> OrderValidationResult:
        if order.session != self.session:
            return OrderValidationResult(False, f"Order outside session: {order.session}")
        return OrderValidationResult(True)

    def _validate_order(self, order: Order) -> OrderValidationResult:
        if not order.symbol:
            return OrderValidationResult(False, "Missing symbol")
        if not order.security_id:
            return OrderValidationResult(False, "Missing security_id")
        if order.side not in [Side.BUY, Side.SELL]:
            return OrderValidationResult(False, f"Invalid side: {order.side}")
        if order.quantity <= 0:
            return OrderValidationResult(False, f"Invalid quantity: {order.quantity}")
        if order.order_type != OrderType.LIMIT:
            return OrderValidationResult(False, f"Unsupported order type: {order.order_type}")
        if order.price is None:
            return OrderValidationResult(False, "Missing premium for priced order type")
        return OrderValidationResult(True)

    def _validate_price(self, order: Order, book: InstrumentOrderBook) -> OrderValidationResult:
        if not self.price_validator(order, book):
            return OrderValidationResult(False, "Price validation failed")
        return OrderValidationResult(True)

    def _check_cross(self, incoming: Order, book: InstrumentOrderBook) -> bool:
        if incoming.side == Side.BUY:
            best_ask_price, _ = book.get_best_ask()
            if best_ask_price is not None and incoming.price is not None:
                return best_ask_price <= incoming.price
            return False
        else:
            best_bid_price, _ = book.get_best_bid()
            if best_bid_price is not None and incoming.price is not None:
                return best_bid_price >= incoming.price
            return False

    def _match(self, incoming: Order, book: InstrumentOrderBook) -> tuple[Order, list[Trade]]:
        opposite_side = Side.SELL if incoming.side == Side.BUY else Side.BUY
        
        book_side = book.normal_book.get_side(opposite_side)
        
        remaining_qty = incoming.leaves_qty
        trades: list[Trade] = []
        
        while remaining_qty > 0:
            best_price, best_orders = book.get_best_bid() if opposite_side == Side.BUY else book.get_best_ask()
            
            if not best_orders:
                break
            
            if not self._crosses(incoming, best_price):
                break
            
            resting = best_orders[0]
            exec_qty = min(remaining_qty, resting.leaves_qty)
            
            trade = Trade(
                trade_id=str(uuid.uuid4()),
                order_id=incoming.order_id,
                internal_id=incoming.internal_id,
                symbol=incoming.symbol,
                security_id=incoming.security_id,
                side=incoming.side,
                price=resting.price or Decimal("0"),
                quantity=exec_qty,
                counterparty_order_id=resting.order_id,
                counterparty_internal_id=resting.internal_id,
                counterparty_price=resting.price or Decimal("0"),
                exec_time="",
            )
            trades.append(trade)
            
            remaining_qty -= exec_qty
            resting.leaves_qty -= exec_qty
            incoming.cum_qty += exec_qty
            incoming.leaves_qty = remaining_qty
            
            if resting.leaves_qty == 0:
                book.remove_order(resting.internal_id, BookType.NORMAL, resting.side)
                resting.status = OrderStatus.FILLED
                resting.exec_type = ExecType.TRADE
        
        return incoming, trades

    def _crosses(self, incoming: Order, best_price: Decimal | None) -> bool:
        if best_price is None or incoming.price is None:
            return False
        if incoming.side == Side.BUY:
            return best_price <= incoming.price
        else:
            return best_price >= incoming.price

    def _handle_residual(self, incoming: Order, book: InstrumentOrderBook) -> None:
        if incoming.leaves_qty == 0:
            return
        
        if incoming.tif == TimeInForce.IOC:
            incoming.status = OrderStatus.CANCELLED
            incoming.exec_type = ExecType.CANCELED
        else:
            incoming.book = BookType.NORMAL
            book.add_order(incoming)

    def _update_order_status(self, order: Order, trades: list[Trade]) -> None:
        if not trades:
            if order.tif == TimeInForce.IOC:
                order.status = OrderStatus.CANCELLED
            else:
                order.status = OrderStatus.ACTIVE
        elif order.leaves_qty == 0:
            order.status = OrderStatus.FILLED
            order.exec_type = ExecType.TRADE
        else:
            order.status = OrderStatus.PARTIALLY_FILLED
            order.exec_type = ExecType.TRADE

    def process_order(self, order: Order) -> tuple[Order, list[Trade], OrderValidationResult]:
        session_result = self._check_session(order)
        if not session_result.is_valid:
            order.status = OrderStatus.REJECTED
            order.exec_type = ExecType.REPLACED
            return order, [], session_result

        validation_result = self._validate_order(order)
        if not validation_result.is_valid:
            order.status = OrderStatus.REJECTED
            order.exec_type = ExecType.REPLACED
            return order, [], validation_result

        book = self._get_or_create_book(order.symbol, order.security_id)

        price_result = self._validate_price(order, book)
        if not price_result.is_valid:
            order.status = OrderStatus.REJECTED
            order.exec_type = ExecType.REPLACED
            return order, [], price_result

        if not self._check_cross(order, book):
            self._handle_residual(order, book)
            if order.status != OrderStatus.CANCELLED:
                order.status = OrderStatus.ACTIVE
            return order, [], OrderValidationResult(True)

        order.status = OrderStatus.NEW
        order, trades = self._match(order, book)
        
        self._update_order_status(order, trades)
        self.trades.extend(trades)

        if order.status not in [OrderStatus.FILLED, OrderStatus.CANCELLED]:
            self._handle_residual(order, book)

        return order, trades, OrderValidationResult(True)

    def add_reversal(
        self,
        original_trade_id: str,
        reason: str,
    ) -> TradeReversal | None:
        original_trade = None
        for trade in self.trades:
            if trade.trade_id == original_trade_id:
                original_trade = trade
                break
        
        if original_trade is None:
            return None
        
        for existing_reversal in self.reversals:
            if existing_reversal.original_trade_id == original_trade_id:
                return None
        
        reversal = TradeReversal(
            reversal_id=str(uuid.uuid4()),
            original_trade_id=original_trade_id,
            symbol=original_trade.symbol,
            side=original_trade.side,
            price=original_trade.price,
            quantity=original_trade.quantity,
            reason=reason,
            exec_time="",
        )
        self.reversals.append(reversal)
        return reversal

    def add_correction(
        self,
        original_trade_id: str,
        new_price: Decimal,
        new_quantity: int,
        reason: str,
    ) -> TradeCorrection | None:
        original_trade = None
        for trade in self.trades:
            if trade.trade_id == original_trade_id:
                original_trade = trade
                break
        
        if original_trade is None:
            return None
        
        correction = TradeCorrection(
            correction_id=str(uuid.uuid4()),
            original_trade_id=original_trade_id,
            symbol=original_trade.symbol,
            side=original_trade.side,
            new_price=new_price,
            new_quantity=new_quantity,
            reason=reason,
            exec_time="",
        )
        self.corrections.append(correction)
        return correction


def create_order_from_dict(data: dict[str, Any]) -> Order:
    return Order.from_dict(data)
