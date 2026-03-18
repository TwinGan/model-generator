import pytest
from decimal import Decimal
from src.model.engine.orderbook import (
    Order,
    Side,
    OrderType,
    TimeInForce,
    OrderStatus,
    ExecType,
    Action,
    Session,
    BookType,
    BookSide,
    NormalBook,
    StopParkingBook,
    InstrumentOrderBook,
    OrderBookStore,
)


def create_order(
    internal_id: str = "O1",
    order_id: str = "OID1",
    symbol: str = "379306",
    side: Side = Side.BUY,
    price: Decimal = Decimal("100.0"),
    quantity: int = 10,
    time_priority: int = 1000,
    book: BookType = BookType.NORMAL,
) -> Order:
    return Order(
        internal_id=internal_id,
        order_id=order_id,
        symbol=symbol,
        security_id=symbol,
        side=side,
        order_type=OrderType.LIMIT,
        price=price,
        quantity=quantity,
        cum_qty=0,
        leaves_qty=quantity,
        time_priority=time_priority,
        tif=TimeInForce.DAY,
        status=OrderStatus.NEW,
        exec_type=ExecType.NEW,
        action=Action.NEW,
        session=Session.OPEN,
        book=book,
        user="test_user",
        broker_client_id="test_broker",
    )


class TestBookSide:
    def test_add_order_bid(self):
        side = BookSide(Side.BUY)
        order = create_order(side=Side.BUY, price=Decimal("100.0"), time_priority=1000)
        side.add_order(order)
        
        assert side.get_order("O1") is not None
        assert side.get_best_price() == Decimal("100.0")

    def test_add_order_ask(self):
        side = BookSide(Side.SELL)
        order = create_order(side=Side.SELL, price=Decimal("100.0"), time_priority=1000)
        side.add_order(order)
        
        assert side.get_order("O1") is not None
        assert side.get_best_price() == Decimal("100.0")

    def test_remove_order(self):
        side = BookSide(Side.BUY)
        order = create_order()
        side.add_order(order)
        
        removed = side.remove_order("O1")
        assert removed is not None
        assert side.get_order("O1") is None

    def test_price_time_priority_bid(self):
        side = BookSide(Side.BUY)
        
        order1 = create_order(internal_id="O1", price=Decimal("100.0"), time_priority=2000)
        order2 = create_order(internal_id="O2", price=Decimal("101.0"), time_priority=1000)
        order3 = create_order(internal_id="O3", price=Decimal("100.0"), time_priority=1000)
        
        side.add_order(order1)
        side.add_order(order2)
        side.add_order(order3)
        
        best_price = side.get_best_price()
        assert best_price == Decimal("101.0")
        
        best_orders = side.get_best_orders()
        assert len(best_orders) == 1
        assert best_orders[0].internal_id == "O2"

    def test_price_time_priority_ask(self):
        side = BookSide(Side.SELL)
        
        order1 = create_order(internal_id="O1", side=Side.SELL, price=Decimal("100.0"), time_priority=1000)
        order2 = create_order(internal_id="O2", side=Side.SELL, price=Decimal("99.0"), time_priority=2000)
        order3 = create_order(internal_id="O3", side=Side.SELL, price=Decimal("100.0"), time_priority=2000)
        
        side.add_order(order1)
        side.add_order(order2)
        side.add_order(order3)
        
        best_price = side.get_best_price()
        assert best_price == Decimal("99.0")
        
        best_orders = side.get_best_orders()
        assert len(best_orders) == 1
        assert best_orders[0].internal_id == "O2"

    def test_same_price_fifo(self):
        side = BookSide(Side.BUY)
        
        order1 = create_order(internal_id="O1", price=Decimal("100.0"), time_priority=1000)
        order2 = create_order(internal_id="O2", price=Decimal("100.0"), time_priority=2000)
        
        side.add_order(order1)
        side.add_order(order2)
        
        best_orders = side.get_best_orders()
        assert len(best_orders) == 2
        assert (best_orders[0].time_priority or 0) < (best_orders[1].time_priority or 0)


class TestNormalBook:
    def test_get_side(self):
        book = NormalBook()
        
        bid = book.get_side(Side.BUY)
        assert bid.side == Side.BUY
        
        ask = book.get_side(Side.SELL)
        assert ask.side == Side.SELL

    def test_add_orders_to_both_sides(self):
        book = NormalBook()
        
        bid_order = create_order(side=Side.BUY, price=Decimal("100.0"))
        ask_order = create_order(side=Side.SELL, price=Decimal("101.0"))
        
        book.bid.add_order(bid_order)
        book.ask.add_order(ask_order)
        
        assert book.bid.get_best_price() == Decimal("100.0")
        assert book.ask.get_best_price() == Decimal("101.0")


class TestInstrumentOrderBook:
    def test_add_order(self):
        book = InstrumentOrderBook("379306", "379306")
        
        order = create_order(side=Side.BUY, price=Decimal("100.0"))
        book.add_order(order)
        
        assert book.normal_book.bid.get_order("O1") is not None

    def test_remove_order(self):
        book = InstrumentOrderBook("379306", "379306")
        
        order = create_order()
        book.add_order(order)
        
        removed = book.remove_order("O1", BookType.NORMAL, Side.BUY)
        assert removed is not None
        assert book.normal_book.bid.get_order("O1") is None

    def test_get_best_bid_ask(self):
        book = InstrumentOrderBook("379306", "379306")
        
        bid1 = create_order(internal_id="B1", side=Side.BUY, price=Decimal("100.0"), time_priority=1000)
        bid2 = create_order(internal_id="B2", side=Side.BUY, price=Decimal("101.0"), time_priority=2000)
        ask1 = create_order(internal_id="A1", side=Side.SELL, price=Decimal("102.0"), time_priority=1000)
        ask2 = create_order(internal_id="A2", side=Side.SELL, price=Decimal("101.0"), time_priority=2000)
        
        book.add_order(bid1)
        book.add_order(bid2)
        book.add_order(ask1)
        book.add_order(ask2)
        
        best_bid_price, best_bid_orders = book.get_best_bid()
        best_ask_price, best_ask_orders = book.get_best_ask()
        
        assert best_bid_price == Decimal("101.0")
        assert best_bid_orders[0].internal_id == "B2"
        assert best_ask_price == Decimal("101.0")
        assert best_ask_orders[0].internal_id == "A2"

    def test_replace_order(self):
        book = InstrumentOrderBook("379306", "379306")
        
        order = create_order(price=Decimal("100.0"))
        book.add_order(order)
        
        new_order = create_order(internal_id="O1", price=Decimal("101.0"))
        book.replace_order(new_order)
        
        replaced = book.normal_book.bid.get_order("O1")
        assert replaced is not None
        assert replaced.price == Decimal("101.0")

    def test_activate_stop_order(self):
        book = InstrumentOrderBook("379306", "379306")
        
        stop_order = create_order(
            internal_id="STOP1",
            side=Side.BUY,
            price=Decimal("100.0"),
            book=BookType.STOP_PARKING,
        )
        book.add_order(stop_order)
        
        activated = book.activate_stop_order("STOP1", Side.BUY)
        
        assert activated is not None
        assert activated.book == BookType.NORMAL
        assert activated.activated is True
        assert book.normal_book.bid.get_order("STOP1") is not None
        assert book.stop_parking.buy_stop.get_order("STOP1") is None

    def test_get_order_by_id(self):
        book = InstrumentOrderBook("379306", "379306")
        
        order1 = create_order(internal_id="O1", side=Side.BUY)
        order2 = create_order(internal_id="O2", side=Side.SELL)
        
        book.add_order(order1)
        book.add_order(order2)
        
        assert book.get_order("O1") is not None
        assert book.get_order("O2") is not None
        assert book.get_order("O3") is None


class TestOrderBookStore:
    def test_load_from_file(self, tmp_path):
        data = {
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [
                            {
                                "ID": "O1",
                                "OrderID": "OID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "BUY",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 10,
                                "CumQty": 0,
                                "LeavesQty": 10,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "test_broker",
                            }
                        ],
                        "SELL": []
                    }
                }
            }
        }
        
        file_path = tmp_path / "test_orderbook.json"
        import json
        file_path.write_text(json.dumps(data))
        
        store = OrderBookStore.load_from_file(str(file_path))
        
        book = store.get_book("379306")
        assert book is not None
        assert book.normal_book.bid.get_best_price() == Decimal("100.0")


class TestOrderFromDict:
    def test_parse_order(self):
        data = {
            "ID": "O1",
            "OrderID": "OID1",
            "Symbol": "379306",
            "SecurityID": "379306",
            "Side": "BUY",
            "OrderType": "LIMIT",
            "Price": "100.0",
            "OrderQty": 10,
            "CumQty": 5,
            "LeavesQty": 5,
            "#TimePriority": 1000,
            "TIF": "DAY",
            "OrdStatus": "PARTIALLY_FILLED",
            "ExecType": "TRADE",
            "Action": "NEW",
            "session": "OPEN",
            "book": "normal_book",
            "User": "test",
            "BrokerClientID": "test_broker",
            "StopPx": "90.0",
            "TriggerType": 4,
            "TriggerPriceType": 2,
            "Activated": "TRUE",
        }
        
        order = Order.from_dict(data)
        
        assert order.internal_id == "O1"
        assert order.order_id == "OID1"
        assert order.side == Side.BUY
        assert order.price == Decimal("100.0")
        assert order.quantity == 10
        assert order.cum_qty == 5
        assert order.leaves_qty == 5
        assert order.status == OrderStatus.PARTIALLY_FILLED
        assert order.stop_price == Decimal("90.0")
        assert order.trigger_type == 4
        assert order.activated is True

    def test_order_to_dict_roundtrip(self):
        data = {
            "ID": "O1",
            "OrderID": "OID1",
            "Symbol": "379306",
            "SecurityID": "379306",
            "Side": "BUY",
            "OrderType": "LIMIT",
            "Price": "100.0",
            "OrderQty": 10,
            "CumQty": 0,
            "LeavesQty": 10,
            "#TimePriority": 1000,
            "TIF": "DAY",
            "OrdStatus": "NEW",
            "ExecType": "NEW",
            "Action": "NEW",
            "session": "OPEN",
            "book": "normal_book",
            "User": "test",
            "BrokerClientID": "test_broker",
        }
        
        order = Order.from_dict(data)
        result = order.to_dict()
        
        assert result["ID"] == "O1"
        assert result["OrderID"] == "OID1"
        assert result["Side"] == "BUY"
        assert result["Price"] == "100.0"
