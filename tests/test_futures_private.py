import os

from binance.client import Client
from tests.utils import load_json_config


class TestFutures:
    def setup_class(self):
        secret = load_json_config(os.path.join(os.path.dirname(__file__), 'secret.json'))
        self.test_client = Client(**secret['binance-test'], test=True)

    def test_account_data(self):
        account = self.test_client.futures_account()
        print(account)

    def test_balance(self):
        balance = self.test_client.futures_account_balance()
        print(balance)

    def test_position_risk(self):
        position = self.test_client.futures_position_information()
        print(position)

    def test_create_order(self):
        order_res = self.test_client.futures_create_order(symbol='BTCUSDT',
                                                          type='LIMIT',
                                                          positionSide='LONG',
                                                          side='BUY',
                                                          price=30000,
                                                          quantity=0.001,
                                                          timeInForce='GTC')
        print(order_res)

    def test_create_batch_orders(self):
        order_res = self.test_client.futures_create_order(batchOrders=[
            {"symbol": 'BTCUSDT', "type": "LIMIT", "positionSide": "LONG", "side": "BUY", "price": 30000,
             "quantity": 0.001, "timeInForce": 'GTC'},
            {"symbol": 'BTCUSDT', "type": "LIMIT", "positionSide": "LONG", "side": "BUY", "price": 30001,
             "quantity": 0.001, "timeInForce": 'GTC'}
        ])
        print(order_res)
