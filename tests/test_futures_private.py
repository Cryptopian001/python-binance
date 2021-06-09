import os

from binance.client import Client
from tests.utils import load_json_config

symbol = 'BTCUSDT'


class TestFutures:
    def setup_class(self):
        secret = load_json_config(os.path.join(os.path.dirname(__file__), 'secret.json'))
        self.test_client = Client(**secret['binance-test'], testnet=True)
        print(self.test_client.futures_cancel_all_open_orders(symbol=symbol))

    def teardown_class(self):
        open_orders = self.test_client.futures_get_open_orders(symbol=symbol)
        print(self.test_client.futures_cancel_all_open_orders(symbol=symbol))
        print(open_orders)
        assert len(open_orders) == 0

    def test_account_data(self):
        account = self.test_client.futures_account()
        # print(account)

    def test_balance(self):
        balance = self.test_client.futures_account_balance()
        # print(balance)

    def test_position_risk(self):
        position = self.test_client.futures_position_information()
        # print(position)

    def test_create_order(self):
        order_res = self.test_client.futures_create_order(symbol=symbol,
                                                          type='LIMIT',
                                                          positionSide='LONG',
                                                          side='BUY',
                                                          price=20000,
                                                          quantity=0.001,
                                                          timeInForce='GTC')
        print('NEW ORDER', order_res)
        open_orders = self.test_client.futures_get_open_orders(symbol=symbol)
        assert len(open_orders) == 1
        print('CANCEL ORDER', self.test_client.futures_cancel_order(symbol=symbol, orderId=order_res['orderId']))

    def test_create_batch_orders(self):
        order_res = self.test_client.futures_place_batch_order(batchOrders=[
            {"symbol": symbol, "type": "LIMIT", "positionSide": "LONG", "side": "BUY", "price": '20000',
             "quantity": '0.001', "timeInForce": 'GTC'},
            {"symbol": symbol, "type": "LIMIT", "positionSide": "LONG", "side": "BUY", "price": '20001',
             "quantity": '0.001', "timeInForce": 'GTC'}
        ])
        print('NEW BATCH ORDERS', order_res)
        open_orders = self.test_client.futures_get_open_orders(symbol=symbol)
        assert len(open_orders) == 2
        origOrderIdList
        print('CANCEL BATCH ORDER', self.test_client.futures_cancel_orders(symbol=symbol, orderId=order_res['orderId']))
