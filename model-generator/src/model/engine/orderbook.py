from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Any
import json


class Side(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    LIMIT = "LIMIT"
    STOPLIMIT = "STOPLIMIT"


class TimeInForce(str, Enum):
    DAY = "DAY"
    GTC = "GTC"
    GTD = "GTD"
    IOC = "IOC"
    FOK = "FOK"


class OrderStatus(str, Enum):
    NEW = "NEW"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    REJECTED = "REJECTED"
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"


class ExecType(str, Enum):
    NEW = "NEW"
    REPLACED = "REPLACED"
    TRADE = "TRADE"
    ACTIVATED = "ACTIVATED"
    CANCELED = "CANCELED"


class Action(str, Enum):
    NEW = "NEW"
    AMEND = "AMEND"
    CANCEL = "CANCEL"


class Session(str, Enum):
    PRE_OPEN = "PRE-OPEN"
    OPEN = "OPEN"


class BookType(str, Enum):
    NORMAL = "normal_book"
    STOP_PARKING = "STOP_PARKING"


def _parse_bool(value: Any) -> bool | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        if value.upper() == "TRUE":
            return True
        elif value.upper() == "FALSE":
            return False
    return None


def _parse_int(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None
    return None


def _parse_decimal(value: Any) -> Decimal | None:
    if value is None:
        return None
    if isinstance(value, Decimal):
        return value
    if isinstance(value, (int, float)):
        return Decimal(str(value))
    if isinstance(value, str):
        try:
            return Decimal(value)
        except ValueError:
            return None
    return None


@dataclass
class Order:
    internal_id: str
    order_id: str
    symbol: str
    security_id: str
    side: Side
    order_type: OrderType
    price: Decimal | None
    quantity: int
    cum_qty: int
    leaves_qty: int
    time_priority: int | None
    tif: TimeInForce
    status: OrderStatus
    exec_type: ExecType
    action: Action
    session: Session
    book: BookType
    user: str
    broker_client_id: str
    stop_price: Decimal | None = None
    trigger_type: int | None = None
    trigger_price_type: int | None = None
    activated: bool | None = None
    original_id: str | None = None
    previous_id: str | None = None
    orig_time_priority: int | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Order:
        raw_fields = {
            "ID", "OrderID", "Symbol", "SecurityID", "Side", "OrderType",
            "Price", "OrderQty", "CumQty", "LeavesQty", "#TimePriority",
            "TIF", "OrdStatus", "ExecType", "Action", "session", "book",
            "User", "BrokerClientID", "StopPx", "TriggerType", "TriggerPriceType",
            "Activated", "OriginalID", "PreviousID", "#OrigTimePriority"
        }
        raw = {k: v for k, v in data.items() if k not in raw_fields}

        return cls(
            internal_id=data.get("ID", ""),
            order_id=data.get("OrderID", ""),
            symbol=data.get("Symbol", data.get("SecurityID", "")),
            security_id=data.get("SecurityID", ""),
            side=Side(data.get("Side", "BUY")),
            order_type=OrderType(data.get("OrderType", "LIMIT")),
            price=_parse_decimal(data.get("Price")),
            quantity=_parse_int(data.get("OrderQty")) or 0,
            cum_qty=_parse_int(data.get("CumQty")) or 0,
            leaves_qty=_parse_int(data.get("LeavesQty")) or 0,
            time_priority=_parse_int(data.get("#TimePriority")),
            tif=TimeInForce(data.get("TIF", "DAY")),
            status=OrderStatus(data.get("OrdStatus", "NEW")),
            exec_type=ExecType(data.get("ExecType", "NEW")),
            action=Action(data.get("Action", "NEW")),
            session=Session(data.get("session", "PRE-OPEN")),
            book=BookType(data.get("book", "normal_book")),
            user=data.get("User", ""),
            broker_client_id=data.get("BrokerClientID", ""),
            stop_price=_parse_decimal(data.get("StopPx")),
            trigger_type=_parse_int(data.get("TriggerType")),
            trigger_price_type=_parse_int(data.get("TriggerPriceType")),
            activated=_parse_bool(data.get("Activated")),
            original_id=data.get("OriginalID"),
            previous_id=data.get("PreviousID"),
            orig_time_priority=_parse_int(data.get("#OrigTimePriority")),
            raw=raw
        )

    def to_dict(self) -> dict[str, Any]:
        result = {
            "ID": self.internal_id,
            "OrderID": self.order_id,
            "Symbol": self.symbol,
            "SecurityID": self.security_id,
            "Side": self.side.value,
            "OrderType": self.order_type.value,
            "Price": str(self.price) if self.price is not None else None,
            "OrderQty": self.quantity,
            "CumQty": self.cum_qty,
            "LeavesQty": self.leaves_qty,
            "#TimePriority": self.time_priority,
            "TIF": self.tif.value,
            "OrdStatus": self.status.value,
            "ExecType": self.exec_type.value,
            "Action": self.action.value,
            "session": self.session.value,
            "book": self.book.value,
            "User": self.user,
            "BrokerClientID": self.broker_client_id,
        }
        if self.stop_price is not None:
            result["StopPx"] = str(self.stop_price)
        if self.trigger_type is not None:
            result["TriggerType"] = self.trigger_type
        if self.trigger_price_type is not None:
            result["TriggerPriceType"] = self.trigger_price_type
        if self.activated is not None:
            result["Activated"] = "TRUE" if self.activated else "FALSE"
        if self.original_id is not None:
            result["OriginalID"] = self.original_id
        if self.previous_id is not None:
            result["PreviousID"] = self.previous_id
        if self.orig_time_priority is not None:
            result["#OrigTimePriority"] = self.orig_time_priority
        result.update(self.raw)
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class ExecutedOrderSummary:
    order_id: str
    user: str
    side: Side
    symbol: str
    broker_client_id: str
    order_qty: int
    cum_qty: int
    exec_type: ExecType
    last_trade: str
    number_of_trades: int
    book: BookType

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ExecutedOrderSummary:
        book_str = data.get("book", "normal_book")
        if book_str == "order_cache":
            book_type = BookType.NORMAL
        else:
            book_type = BookType(book_str)
        return cls(
            order_id=data.get("OrderID", ""),
            user=data.get("User", ""),
            side=Side(data.get("Side", "BUY")),
            symbol=data.get("Symbol", ""),
            broker_client_id=data.get("BrokerClientID", ""),
            order_qty=_parse_int(data.get("OrderQty")) or 0,
            cum_qty=_parse_int(data.get("CumQty")) or 0,
            exec_type=ExecType(data.get("ExecType", "TRADE")),
            last_trade=data.get("LastTrade", ""),
            number_of_trades=_parse_int(data.get("NumberOfTrades")) or 0,
            book=book_type,
        )


class BookSide:
    def __init__(self, side: Side):
        self.side = side
        self._orders: dict[str, Order] = {}
        self._price_levels: dict[Decimal, list[Order]] = {}

    def _get_sort_key(self, order: Order) -> tuple:
        price = order.price if order.price is not None else Decimal('0')
        if self.side == Side.BUY:
            return (-price, order.time_priority or 0)
        else:
            return (price, order.time_priority or 0)

    def _rebuild_price_levels(self):
        self._price_levels.clear()
        for order in self._orders.values():
            if order.price is not None:
                if order.price not in self._price_levels:
                    self._price_levels[order.price] = []
                self._price_levels[order.price].append(order)
        for price_level in self._price_levels.values():
            price_level.sort(key=self._get_sort_key)

    def add_order(self, order: Order) -> None:
        self._orders[order.internal_id] = order
        self._rebuild_price_levels()

    def remove_order(self, internal_id: str) -> Order | None:
        order = self._orders.pop(internal_id, None)
        if order:
            self._rebuild_price_levels()
        return order

    def get_order(self, internal_id: str) -> Order | None:
        return self._orders.get(internal_id)

    def get_all_orders(self) -> list[Order]:
        return list(self._orders.values())

    def get_best_price(self) -> Decimal | None:
        if not self._price_levels:
            return None
        prices = sorted(self._price_levels.keys())
        if self.side == Side.BUY:
            return prices[-1]
        else:
            return prices[0]

    def get_best_orders(self) -> list[Order]:
        best_price = self.get_best_price()
        if best_price is None:
            return []
        return list(self._price_levels.get(best_price, []))

    def get_orders_at_price(self, price: Decimal) -> list[Order]:
        return list(self._price_levels.get(price, []))

    def get_price_levels(self) -> list[Decimal]:
        return sorted(self._price_levels.keys(), reverse=(self.side == Side.BUY))

    def get_total_quantity_at_price(self, price: Decimal) -> int:
        return sum(o.leaves_qty for o in self._price_levels.get(price, []))


class NormalBook:
    def __init__(self):
        self.bid = BookSide(Side.BUY)
        self.ask = BookSide(Side.SELL)

    def get_side(self, side: Side) -> BookSide:
        return self.bid if side == Side.BUY else self.ask


class StopParkingBook:
    def __init__(self):
        self.buy_stop = BookSide(Side.BUY)
        self.sell_stop = BookSide(Side.SELL)

    def get_side(self, side: Side) -> BookSide:
        return self.buy_stop if side == Side.BUY else self.sell_stop


class InstrumentOrderBook:
    def __init__(self, symbol: str, security_id: str):
        self.symbol = symbol
        self.security_id = security_id
        self.normal_book = NormalBook()
        self.stop_parking = StopParkingBook()
        self.order_cache: dict[str, ExecutedOrderSummary] = {}

    def add_order(self, order: Order) -> None:
        if order.book == BookType.NORMAL:
            book_side = self.normal_book.get_side(order.side)
            book_side.add_order(order)
        elif order.book == BookType.STOP_PARKING:
            book_side = self.stop_parking.get_side(order.side)
            book_side.add_order(order)

    def remove_order(self, internal_id: str, book: BookType, side: Side) -> Order | None:
        if book == BookType.NORMAL:
            return self.normal_book.get_side(side).remove_order(internal_id)
        elif book == BookType.STOP_PARKING:
            return self.stop_parking.get_side(side).remove_order(internal_id)
        return None

    def replace_order(self, order: Order) -> None:
        old_order = self.remove_order(order.internal_id, order.book, order.side)
        if old_order:
            self.add_order(order)

    def activate_stop_order(self, internal_id: str, side: Side) -> Order | None:
        order = self.stop_parking.get_side(side).remove_order(internal_id)
        if order is None:
            return None
        order.book = BookType.NORMAL
        order.activated = True
        order.exec_type = ExecType.ACTIVATED
        self.normal_book.get_side(order.side).add_order(order)
        return order

    def get_order(self, internal_id: str) -> Order | None:
        for side in [Side.BUY, Side.SELL]:
            order = self.normal_book.get_side(side).get_order(internal_id)
            if order:
                return order
            order = self.stop_parking.get_side(side).get_order(internal_id)
            if order:
                return order
        return None

    def get_best_bid(self) -> tuple[Decimal | None, list[Order]]:
        best_price = self.normal_book.bid.get_best_price()
        if best_price is None:
            return None, []
        return best_price, self.normal_book.bid.get_best_orders()

    def get_best_ask(self) -> tuple[Decimal | None, list[Order]]:
        best_price = self.normal_book.ask.get_best_price()
        if best_price is None:
            return None, []
        return best_price, self.normal_book.ask.get_best_orders()

    def get_bid_levels(self) -> list[Decimal]:
        return self.normal_book.bid.get_price_levels()

    def get_ask_levels(self) -> list[Decimal]:
        return self.normal_book.ask.get_price_levels()

    def add_execution_summary(self, summary: ExecutedOrderSummary) -> None:
        self.order_cache[summary.order_id] = summary

    def get_execution_summary(self, order_id: str) -> ExecutedOrderSummary | None:
        return self.order_cache.get(order_id)

    def to_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "security_id": self.security_id,
            "normal_book": {
                "BUY": [o.to_dict() for o in self.normal_book.bid.get_all_orders()],
                "SELL": [o.to_dict() for o in self.normal_book.ask.get_all_orders()],
            },
            "STOP_PARKING": {
                "BUY": [o.to_dict() for o in self.stop_parking.buy_stop.get_all_orders()],
                "SELL": [o.to_dict() for o in self.stop_parking.sell_stop.get_all_orders()],
            },
            "order_cache": [s.__dict__ for s in self.order_cache.values()],
        }


class OrderBookStore:
    def __init__(self):
        self.books: dict[str, InstrumentOrderBook] = {}

    def add_book(self, symbol: str, security_id: str) -> InstrumentOrderBook:
        book = InstrumentOrderBook(symbol, security_id)
        self.books[symbol] = book
        return book

    def get_book(self, symbol: str) -> InstrumentOrderBook | None:
        return self.books.get(symbol)

    def load_from_dict(self, data: dict[str, Any]) -> None:
        bookshelf = data.get("BOOKSHELF_STATE", {})
        for security_id, instrument_data in bookshelf.items():
            normal_book_data = instrument_data.get("normal_book", {})
            
            buy_orders = normal_book_data.get("BUY", [])
            sell_orders = normal_book_data.get("SELL", [])
            
            symbol = None
            if buy_orders:
                symbol = buy_orders[0].get("Symbol")
            if not symbol and sell_orders:
                symbol = sell_orders[0].get("Symbol")
            if not symbol:
                symbol = security_id
            
            book = self.add_book(symbol, security_id)
            
            for order_data in buy_orders:
                order = Order.from_dict(order_data)
                book.add_order(order)
            
            for order_data in sell_orders:
                order = Order.from_dict(order_data)
                book.add_order(order)
            
            stop_parking_data = normal_book_data.get("STOP_PARKING", [])
            for order_data in stop_parking_data:
                order = Order.from_dict(order_data)
                book.add_order(order)
            
            for summary_data in instrument_data.get("order_cache", []):
                summary = ExecutedOrderSummary.from_dict(summary_data)
                book.add_execution_summary(summary)

    @classmethod
    def load_from_file(cls, filepath: str) -> OrderBookStore:
        store = cls()
        with open(filepath, "r") as f:
            data = json.load(f)
        store.load_from_dict(data)
        return store

    def to_dict(self) -> dict[str, Any]:
        result = {}
        for symbol, book in self.books.items():
            result[symbol] = book.to_dict()
        return result
