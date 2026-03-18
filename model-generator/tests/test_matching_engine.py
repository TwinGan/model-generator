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
    OrderBookStore,
)
from src.model.engine.matching_engine import (
    MatchingEngine,
    Trade,
    TradeReversal,
    TradeCorrection,
    OrderValidationResult,
    create_order_from_dict,
)


def create_test_order(
    internal_id: str = "O1",
    order_id: str = "OID1",
    symbol: str = "379306",
    security_id: str = "379306",
    side: Side = Side.BUY,
    price: Decimal = Decimal("100.0"),
    quantity: int = 10,
    order_type: OrderType = OrderType.LIMIT,
    tif: TimeInForce = TimeInForce.DAY,
    time_priority: int = 1000,
    session: Session = Session.OPEN,
) -> Order:
    return Order(
        internal_id=internal_id,
        order_id=order_id,
        symbol=symbol,
        security_id=security_id,
        side=side,
        order_type=order_type,
        price=price,
        quantity=quantity,
        cum_qty=0,
        leaves_qty=quantity,
        time_priority=time_priority,
        tif=tif,
        status=OrderStatus.NEW,
        exec_type=ExecType.NEW,
        action=Action.NEW,
        session=session,
        book=BookType.NORMAL,
        user="test_user",
        broker_client_id="test_broker",
    )


def always_valid_price(order: Order, book) -> bool:
    return True


def always_invalid_price(order: Order, book) -> bool:
    return False


class TestMatchingEngineRejection:
    def test_reject_order_outside_session(self):
        store = OrderBookStore()
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        order = create_test_order(session=Session.PRE_OPEN)
        
        result_order, trades, validation = engine.process_order(order)
        
        assert validation.is_valid is False
        assert "outside session" in validation.reject_reason
        assert result_order.status == OrderStatus.REJECTED

    def test_reject_unsupported_order_type(self):
        store = OrderBookStore()
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        order = create_test_order(order_type=OrderType.STOPLIMIT)
        
        result_order, trades, validation = engine.process_order(order)
        
        assert validation.is_valid is False
        assert "Unsupported order type" in validation.reject_reason
        assert result_order.status == OrderStatus.REJECTED

    def test_reject_invalid_quantity(self):
        store = OrderBookStore()
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        order = create_test_order(quantity=0)
        
        result_order, trades, validation = engine.process_order(order)
        
        assert validation.is_valid is False
        assert "Invalid quantity" in validation.reject_reason

    def test_reject_missing_price_for_limit_order(self):
        store = OrderBookStore()
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        order = create_test_order(price=None)
        
        result_order, trades, validation = engine.process_order(order)
        
        assert validation.is_valid is False
        assert "Missing premium" in validation.reject_reason

    def test_reject_failed_price_validation(self):
        store = OrderBookStore()
        engine = MatchingEngine(store, always_invalid_price, Session.OPEN)
        
        order = create_test_order()
        
        result_order, trades, validation = engine.process_order(order)
        
        assert validation.is_valid is False
        assert "Price validation failed" in validation.reject_reason
        assert result_order.status == OrderStatus.REJECTED


class TestMatchingEngineBuyCross:
    def test_buy_order_crosses_best_ask(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("101.0"),
            quantity=5,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert validation.is_valid is True
        assert len(trades) == 1
        assert trades[0].price == Decimal("100.0")
        assert trades[0].quantity == 5
        assert result_order.status == OrderStatus.FILLED

    def test_sell_order_crosses_best_bid(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "BUY",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "SELL": [],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.SELL,
            price=Decimal("99.0"),
            quantity=5,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert validation.is_valid is True
        assert len(trades) == 1
        assert trades[0].price == Decimal("100.0")
        assert trades[0].quantity == 5
        assert result_order.status == OrderStatus.FILLED


class TestMatchingEngineNonCross:
    def test_non_crossing_limit_order_rests_on_book(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "105.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("100.0"),
            quantity=5,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert validation.is_valid is True
        assert len(trades) == 0
        assert result_order.status == OrderStatus.ACTIVE
        
        book = store.get_book("379306")
        assert book.normal_book.bid.get_order("IN1") is not None

    def test_non_crossing_ioc_order_is_cancelled(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "105.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("100.0"),
            quantity=5,
            tif=TimeInForce.IOC,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert validation.is_valid is True
        assert len(trades) == 0
        assert result_order.status == OrderStatus.CANCELLED
        
        book = store.get_book("379306")
        assert book.normal_book.bid.get_order("IN1") is None


class TestMatchingEnginePartialFill:
    def test_partial_fill_against_one_resting_order(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("101.0"),
            quantity=10,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert validation.is_valid is True
        assert len(trades) == 1
        assert trades[0].quantity == 5
        assert result_order.status == OrderStatus.PARTIALLY_FILLED
        assert result_order.leaves_qty == 5

    def test_full_fill_against_one_resting_order(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
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
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("101.0"),
            quantity=10,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert validation.is_valid is True
        assert len(trades) == 1
        assert trades[0].quantity == 10
        assert result_order.status == OrderStatus.FILLED
        
        book = store.get_book("379306")
        assert book.normal_book.ask.get_order("REST1") is None

    def test_one_incoming_fills_multiple_resting_orders(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            },
                            {
                                "ID": "REST2",
                                "OrderID": "ROID2",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "101.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 2000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("102.0"),
            quantity=10,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert validation.is_valid is True
        assert len(trades) == 2
        assert trades[0].price == Decimal("100.0")
        assert trades[0].quantity == 5
        assert trades[1].price == Decimal("101.0")
        assert trades[1].quantity == 5
        assert result_order.status == OrderStatus.FILLED


class TestMatchingEngineExecutionPrice:
    def test_execution_price_equals_resting_order_price(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.50",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("105.00"),
            quantity=5,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert len(trades) == 1
        assert trades[0].price == Decimal("100.50")
        assert trades[0].counterparty_price == Decimal("100.50")


class TestMatchingEngineFIFO:
    def test_same_price_fifo_priority(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 3,
                                "CumQty": 0,
                                "LeavesQty": 3,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            },
                            {
                                "ID": "REST2",
                                "OrderID": "ROID2",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 3,
                                "CumQty": 0,
                                "LeavesQty": 3,
                                "#TimePriority": 2000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test2",
                                "BrokerClientID": "broker2",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("101.0"),
            quantity=3,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        assert len(trades) == 1
        assert trades[0].counterparty_internal_id == "REST1"


class TestMatchingEngineImmutability:
    def test_trade_records_are_immutable(self):
        store = OrderBookStore()
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("101.0"),
            quantity=5,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        original_trade = trades[0]
        
        with pytest.raises(AttributeError):
            original_trade.quantity = 10

    def test_add_reversal_record(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("101.0"),
            quantity=5,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        original_trade_id = trades[0].trade_id
        
        reversal = engine.add_reversal(original_trade_id, "Error trade")
        
        assert reversal is not None
        assert reversal.original_trade_id == original_trade_id
        assert reversal.quantity == 5

    def test_add_correction_record(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("101.0"),
            quantity=5,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        original_trade_id = trades[0].trade_id
        
        correction = engine.add_correction(
            original_trade_id,
            Decimal("100.50"),
            5,
            "Price correction",
        )
        
        assert correction is not None
        assert correction.original_trade_id == original_trade_id
        assert correction.new_price == Decimal("100.50")

    def test_no_partial_reversal(self):
        store = OrderBookStore()
        store.load_from_dict({
            "BOOKSHELF_STATE": {
                "379306": {
                    "normal_book": {
                        "BUY": [],
                        "SELL": [
                            {
                                "ID": "REST1",
                                "OrderID": "ROID1",
                                "Symbol": "379306",
                                "SecurityID": "379306",
                                "Side": "SELL",
                                "OrderType": "LIMIT",
                                "Price": "100.0",
                                "OrderQty": 5,
                                "CumQty": 0,
                                "LeavesQty": 5,
                                "#TimePriority": 1000,
                                "TIF": "DAY",
                                "OrdStatus": "NEW",
                                "ExecType": "NEW",
                                "Action": "NEW",
                                "session": "OPEN",
                                "book": "normal_book",
                                "User": "test",
                                "BrokerClientID": "broker",
                            }
                        ],
                        "STOP_PARKING": []
                    },
                    "order_cache": []
                }
            }
        })
        engine = MatchingEngine(store, always_valid_price, Session.OPEN)
        
        incoming = create_test_order(
            internal_id="IN1",
            order_id="IOID1",
            side=Side.BUY,
            price=Decimal("101.0"),
            quantity=5,
        )
        
        result_order, trades, validation = engine.process_order(incoming)
        
        original_trade_id = trades[0].trade_id
        
        reversal = engine.add_reversal(original_trade_id, "Error")
        
        second_reversal = engine.add_reversal(original_trade_id, "Double reversal")
        
        assert second_reversal is None
