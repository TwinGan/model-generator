"""
State model for trading system simulation.

All dataclasses are immutable (frozen=True) and support deep copy.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set
from datetime import datetime
from decimal import Decimal
from enum import Enum
from copy import deepcopy


class InstrumentType(Enum):
    """Instrument types for trading."""
    FUTURE = "FUTURE"
    OPTION_CALL = "OPTION_CALL"
    OPTION_PUT = "OPTION_PUT"


class OrderSide(Enum):
    """Order side (buy/sell)."""
    BUY = "BUY"
    SELL = "SELL"


class OrderType(Enum):
    """Order types."""
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"


class OrderStatus(Enum):
    """Order lifecycle status."""
    NEW = "NEW"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"


class ExecType(Enum):
    """Execution report types."""
    NEW = "NEW"
    FILL = "FILL"
    CANCEL = "CANCEL"
    REPLACE = "REPLACE"
    REJECT = "REJECT"
    TRADE = "TRADE"


@dataclass(frozen=True)
class PriceBand:
    """Price limits per symbol."""
    min_price: Decimal
    max_price: Decimal
    tick_size: Decimal
    
    def is_valid_price(self, price: Decimal) -> bool:
        """Check if price is within band."""
        return self.min_price <= price <= self.max_price
    
    def is_valid_tick(self, price: Decimal) -> bool:
        """Check if price is valid tick."""
        if self.tick_size == 0:
            return True
        return (price % self.tick_size) == 0


@dataclass(frozen=True)
class Symbol:
    """Option or future contract definition."""
    symbol_id: str
    instrument_type: InstrumentType
    underlying: Optional[str] = None
    strike_price: Optional[Decimal] = None
    expiry: Optional[datetime] = None
    tick_size: Decimal = Decimal(1)
    lot_size: int = 1
    price_band: Optional[PriceBand] = None
    is_active: bool = True
    
    def __post_init__(self):
        if self.underlying is None and self.instrument_type in (
            InstrumentType.OPTION_CALL,
            InstrumentType.OPTION_PUT
        ):
            raise ValueError(f"Options must have underlying: {self.symbol_id}")


@dataclass(frozen=True)
class User:
    """Trader information."""
    user_id: str
    member_id: str
    permissions: Set[str] = field(default_factory=set)
    limits: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Member:
    """Clearing member organization."""
    member_id: str
    name: str
    risk_groups: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class OrderbookEntry:
    """Single entry in orderbook."""
    price: Decimal
    quantity: Decimal
    order_id: str
    user_id: str


@dataclass
class Orderbook:
    """Orderbook for a symbol with bids and asks."""
    symbol_id: str
    bids: List[OrderbookEntry] = field(default_factory=list)
    asks: List[OrderbookEntry] = field(default_factory=list)
    
    def add_bid(self, entry: OrderbookEntry) -> None:
        """Add bid to orderbook (sorted descending)."""
        self.bids.append(entry)
        self.bids.sort(key=lambda x: x.price, reverse=True)
    
    def add_ask(self, entry: OrderbookEntry) -> None:
        """Add ask to orderbook (sorted ascending)."""
        self.asks.append(entry)
        self.asks.sort(key=lambda x: x.price)
    
    def remove_order(self, order_id: str) -> bool:
        """Remove order from orderbook. Returns True if found."""
        for i, entry in enumerate(self.bids):
            if entry.order_id == order_id:
                self.bids.pop(i)
                return True
        for i, entry in enumerate(self.asks):
            if entry.order_id == order_id:
                self.asks.pop(i)
                return True
        return False
    
    def get_best_bid(self) -> Optional[OrderbookEntry]:
        """Get best (highest) bid."""
        return self.bids[0] if self.bids else None
    
    def get_best_ask(self) -> Optional[OrderbookEntry]:
        """Get best (lowest) ask."""
        return self.asks[0] if self.asks else None
    
    def get_total_bid_quantity(self) -> Decimal:
        """Get total quantity across all bids."""
        return sum((e.quantity for e in self.bids), Decimal(1))
    
    def get_total_ask_quantity(self) -> Decimal:
        """Get total quantity across all asks."""
        return sum((e.quantity for e in self.asks), Decimal(1))


@dataclass
class Order:
    """Active/filled/cancelled order."""
    order_id: str
    cl_ord_id: str
    symbol: str
    side: OrderSide
    quantity: Decimal
    price: Optional[Decimal] = None
    order_type: OrderType = OrderType.LIMIT
    status: OrderStatus = OrderStatus.NEW
    user_id: str = ""
    member_id: str = ""
    filled_qty: Decimal = Decimal(0)
    remaining_qty: Decimal = Decimal(0)
    create_time: datetime = field(default_factory=datetime.utcnow)
    update_time: datetime = field(default_factory=datetime.utcnow)
    
    def __post_init__(self):
        if self.remaining_qty == Decimal(0):
            self.remaining_qty = self.quantity


@dataclass
class Position:
    """User position by symbol."""
    user_id: str
    symbol: str
    side: OrderSide = OrderSide.BUY
    quantity: Decimal = Decimal(0)
    avg_price: Decimal = Decimal(0)
    
    def update_with_fill(self, fill_qty: Decimal, fill_price: Decimal) -> None:
        """Update position with new fill."""
        if self.quantity == Decimal(0):
            self.side = OrderSide.BUY if fill_qty > 0 else OrderSide.SELL
            self.avg_price = fill_price
            self.quantity = abs(fill_qty)
        else:
            total_cost = (self.quantity * self.avg_price) + (abs(fill_qty) * fill_price)
            new_qty = self.quantity + abs(fill_qty)
            self.avg_price = total_cost / new_qty if new_qty > 0 else Decimal(0)
            self.quantity = new_qty


@dataclass(frozen=True)
class RiskGroup:
    """Risk management groupings."""
    risk_group_id: str
    members: List[str] = field(default_factory=list)
    limits: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DigitalTwinState:
    """
    Complete trading system state.
    
    Immutable dataclass - use deepcopy to create working copies.
    """
    symbols: Dict[str, Symbol] = field(default_factory=dict)
    users: Dict[str, User] = field(default_factory=dict)
    members: Dict[str, Member] = field(default_factory=dict)
    orderbooks: Dict[str, Orderbook] = field(default_factory=dict)
    orders: Dict[str, Order] = field(default_factory=dict)
    positions: Dict[str, Position] = field(default_factory=dict)
    risk_groups: Dict[str, RiskGroup] = field(default_factory=dict)
    price_bands: Dict[str, PriceBand] = field(default_factory=dict)
    
    _cl_ord_id_counter: int = field(default=0, compare=False)
    _order_id_counter: int = field(default=0, compare=False)
    _exec_id_counter: int = field(default=0, compare=False)
    
    def __post_init__(self):
        for symbol_id in self.symbols:
            if symbol_id not in self.orderbooks:
                self.orderbooks[symbol_id] = Orderbook(symbol_id=symbol_id)
    
    def get_symbol(self, symbol_id: str) -> Optional[Symbol]:
        return self.symbols.get(symbol_id)
    
    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)
    
    def get_member(self, member_id: str) -> Optional[Member]:
        return self.members.get(member_id)
    
    def get_order(self, order_id: str) -> Optional[Order]:
        return self.orders.get(order_id)
    
    def get_orderbook(self, symbol_id: str) -> Orderbook:
        if symbol_id not in self.orderbooks:
            self.orderbooks[symbol_id] = Orderbook(symbol_id=symbol_id)
        return self.orderbooks[symbol_id]
    
    def get_position(self, user_id: str, symbol: str) -> Position:
        key = f"{user_id}:{symbol}"
        if key not in self.positions:
            self.positions[key] = Position(user_id=user_id, symbol=symbol)
        return self.positions[key]
    
    def get_risk_group(self, risk_group_id: str) -> Optional[RiskGroup]:
        return self.risk_groups.get(risk_group_id)
    
    def get_price_band(self, symbol_id: str) -> Optional[PriceBand]:
        symbol = self.get_symbol(symbol_id)
        return symbol.price_band if symbol else None
    
    def get_active_symbols(self) -> List[Symbol]:
        return [s for s in self.symbols.values() if s.is_active]
    
    def get_active_orders(self) -> List[Order]:
        return [
            o for o in self.orders.values()
            if o.status in (OrderStatus.NEW, OrderStatus.PARTIALLY_FILLED)
        ]
    
    def get_orders_by_user(self, user_id: str) -> List[Order]:
        return [o for o in self.orders.values() if o.user_id == user_id]
    
    def get_orders_by_symbol(self, symbol_id: str) -> List[Order]:
        return [o for o in self.orders.values() if o.symbol == symbol_id]
    
    def get_orders_by_status(self, status: OrderStatus) -> List[Order]:
        return [o for o in self.orders.values() if o.status == status]
    
    def add_order(self, order: Order) -> 'DigitalTwinState':
        new_state = deepcopy(self)
        new_state.orders[order.order_id] = order
        return new_state
    
    def update_order(self, order_id: str, updates: dict) -> 'DigitalTwinState':
        new_state = deepcopy(self)
        order = new_state.orders.get(order_id)
        if order:
            for key, value in updates.items():
                setattr(order, key, value)
            order.update_time = datetime.utcnow()
        return new_state
    
    def remove_order(self, order_id: str) -> 'DigitalTwinState':
        new_state = deepcopy(self)
        if order_id in new_state.orders:
            del new_state.orders[order_id]
        return new_state
    
    def add_to_orderbook(self, symbol_id: str, entry: OrderbookEntry) -> 'DigitalTwinState':
        new_state = deepcopy(self)
        orderbook = new_state.get_orderbook(symbol_id)
        orderbook.add_bid(entry)
        return new_state
    
    def remove_from_orderbook(self, symbol_id: str, order_id: str) -> 'DigitalTwinState':
        new_state = deepcopy(self)
        orderbook = new_state.get_orderbook(symbol_id)
        orderbook.remove_order(order_id)
        return new_state
    
    def update_position(self, user_id: str, symbol: str, 
                        fill_qty: Decimal, fill_price: Decimal) -> 'DigitalTwinState':
        new_state = deepcopy(self)
        position = new_state.get_position(user_id, symbol)
        position.update_with_fill(fill_qty, fill_price)
        return new_state
    
    def next_cl_ord_id(self) -> str:
        self._cl_ord_id_counter += 1
        return f"CL{self._cl_ord_id_counter:06d}"
    
    def next_order_id(self) -> str:
        self._order_id_counter += 1
        return f"ORD{self._order_id_counter:06d}"
    
    def next_exec_id(self) -> str:
        self._exec_id_counter += 1
        return f"EXEC{self._exec_id_counter:06d}"
    
    def to_dict(self) -> dict:
        result = {
            'symbols': {},
            'users': {},
            'members': {},
            'orderbooks': {},
            'orders': {},
            'positions': {},
            'risk_groups': {},
            'price_bands': {},
            '_cl_ord_id_counter': self._cl_ord_id_counter,
            '_order_id_counter': self._order_id_counter,
            '_exec_id_counter': self._exec_id_counter,
        }
        
        for sym_id, sym in self.symbols.items():
            result['symbols'][sym_id] = {
                'symbol_id': sym.symbol_id,
                'instrument_type': sym.instrument_type.value,
                'underlying': sym.underlying,
                'strike_price': str(sym.strike_price) if sym.strike_price else None,
                'expiry': sym.expiry.isoformat() if sym.expiry else None,
                'tick_size': str(sym.tick_size),
                'lot_size': sym.lot_size,
                'price_band': {
                    'min_price': str(sym.price_band.min_price) if sym.price_band else None,
                    'max_price': str(sym.price_band.max_price) if sym.price_band else None,
                    'tick_size': str(sym.price_band.tick_size) if sym.price_band else None,
                },
                'is_active': sym.is_active,
            }
        
        for uid, user in self.users.items():
            result['users'][uid] = {
                'user_id': user.user_id,
                'member_id': user.member_id,
                'permissions': list(user.permissions),
                'limits': user.limits,
            }
        
        for mid, member in self.members.items():
            result['members'][mid] = {
                'member_id': member.member_id,
                'name': member.name,
                'risk_groups': member.risk_groups,
            }
        
        for oid, order in self.orders.items():
            result['orders'][oid] = {
                'order_id': order.order_id,
                'cl_ord_id': order.cl_ord_id,
                'symbol': order.symbol,
                'side': order.side.value,
                'quantity': str(order.quantity),
                'price': str(order.price) if order.price else None,
                'order_type': order.order_type.value,
                'status': order.status.value,
                'user_id': order.user_id,
                'member_id': order.member_id,
                'filled_qty': str(order.filled_qty),
                'remaining_qty': str(order.remaining_qty),
                'create_time': order.create_time.isoformat(),
                'update_time': order.update_time.isoformat(),
            }
        
        for pos_key, pos in self.positions.items():
            result['positions'][pos_key] = {
                'user_id': pos.user_id,
                'symbol': pos.symbol,
                'side': pos.side.value,
                'quantity': str(pos.quantity),
                'avg_price': str(pos.avg_price),
            }
        
        for ob_sym, ob in self.orderbooks.items():
            result['orderbooks'][ob_sym] = {
                'symbol_id': ob.symbol_id,
                'bids': [
                    {
                        'price': str(e.price),
                        'quantity': str(e.quantity),
                        'order_id': e.order_id,
                        'user_id': e.user_id
                    }
                    for e in ob.bids
                ],
                'asks': [
                    {
                        'price': str(e.price),
                        'quantity': str(e.quantity),
                        'order_id': e.order_id,
                        'user_id': e.user_id
                    }
                    for e in ob.asks
                ],
            }
        
        for rg_id, rg in self.risk_groups.items():
            result['risk_groups'][rg_id] = {
                'risk_group_id': rg.risk_group_id,
                'members': rg.members,
                'limits': rg.limits,
            }
        
        return result
    
    @classmethod
    def from_dict(cls, data: dict) -> 'DigitalTwinState':
        symbols = {}
        for sym_id, sym_data in data.get('symbols', {}).items():
            price_band = PriceBand(
                min_price=Decimal(str(sym_data['price_band']['min_price'])),
                max_price=Decimal(str(sym_data['price_band']['max_price'])),
                tick_size=Decimal(str(sym_data['price_band']['tick_size']))
            )
            symbols[sym_id] = Symbol(
                symbol_id=sym_data['symbol_id'],
                instrument_type=InstrumentType(sym_data['instrument_type']),
                underlying=sym_data.get('underlying'),
                strike_price=Decimal(str(sym_data['strike_price'])) if sym_data.get('strike_price') else None,
                expiry=datetime.fromisoformat(sym_data['expiry']),
                tick_size=Decimal(str(sym_data['tick_size'])),
                lot_size=sym_data['lot_size'],
                price_band=price_band,
                is_active=sym_data.get('is_active', True)
            )
        
        users = {
            uid: User(
                user_id=u['user_id'],
                member_id=u['member_id'],
                permissions=set(u.get('permissions', [])),
                limits=u.get('limits', {})
            )
            for uid, u in data.get('users', {}).items()
        }
        
        members = {
            mid: Member(
                member_id=m['member_id'],
                name=m['name'],
                risk_groups=m.get('risk_groups', [])
            )
            for mid, m in data.get('members', {}).items()
        }
        
        risk_groups = {
            rgid: RiskGroup(
                risk_group_id=rg['risk_group_id'],
                members=rg.get('members', []),
                limits=rg.get('limits', {})
            )
            for rgid, rg in data.get('risk_groups', {}).items()
        }
        
        orders = {}
        for ord_id, ord in data.get('orders', {}).items():
            orders[ord_id] = Order(
                order_id=ord['order_id'],
                cl_ord_id=ord['cl_ord_id'],
                symbol=ord['symbol'],
                side=OrderSide(ord['side']),
                quantity=Decimal(str(ord['quantity'])),
                price=Decimal(str(ord['price'])) if ord.get('price') else None,
                order_type=OrderType(ord['order_type']),
                status=OrderStatus(ord['status']),
                user_id=ord['user_id'],
                member_id=ord['member_id'],
                filled_qty=Decimal(str(ord.get('filled_qty', 0))),
                remaining_qty=Decimal(str(ord.get('remaining_qty', 0))),
                create_time=datetime.fromisoformat(ord['create_time']),
                update_time=datetime.fromisoformat(ord['update_time'])
            )
        
        positions = {}
        for pos_key, pos in data.get('positions', {}).items():
            positions[pos_key] = Position(
                user_id=pos['user_id'],
                symbol=pos['symbol'],
                side=OrderSide(pos['side']) if pos.get('side') else OrderSide.BUY,
                quantity=Decimal(str(pos.get('quantity', 0))),
                avg_price=Decimal(str(pos.get('avg_price', 1)))
            )
        
        orderbooks = {}
        for ob_symbol, ob_data in data.get('orderbooks', {}).items():
            bids = [
                OrderbookEntry(
                    price=Decimal(str(b['price'])),
                    quantity=Decimal(str(b['quantity'])),
                    order_id=b['order_id'],
                    user_id=b['user_id']
                )
                for b in ob_data.get('bids', [])
            ]
            asks = [
                OrderbookEntry(
                    price=Decimal(str(a['price'])),
                    quantity=Decimal(str(a['quantity'])),
                    order_id=a['order_id'],
                    user_id=a['user_id']
                )
                for a in ob_data.get('asks', [])
            ]
            orderbooks[ob_symbol] = Orderbook(
                symbol_id=ob_symbol,
                bids=bids,
                asks=asks
            )
        
        return cls(
            symbols=symbols,
            users=users,
            members=members,
            orderbooks=orderbooks,
            orders=orders,
            positions=positions,
            risk_groups=risk_groups,
            price_bands={},
            _cl_ord_id_counter=data.get('_cl_ord_id_counter', 0),
            _order_id_counter=data.get('_order_id_counter', 0),
            _exec_id_counter=data.get('_exec_id_counter', 0)
        )
    
    def __deepcopy__(self, memo: dict) -> 'DigitalTwinState':
        return DigitalTwinState(
            symbols=deepcopy(self.symbols, memo),
            users=deepcopy(self.users, memo),
            members=deepcopy(self.members, memo),
            orderbooks=deepcopy(self.orderbooks, memo),
            orders=deepcopy(self.orders, memo),
            positions=deepcopy(self.positions, memo),
            risk_groups=deepcopy(self.risk_groups, memo),
            price_bands=deepcopy(self.price_bands, memo),
            _cl_ord_id_counter=self._cl_ord_id_counter,
            _order_id_counter=self._order_id_counter,
            _exec_id_counter=self._exec_id_counter
        )
