import os

from binance.client import Client
from tests.utils import load_json_config


class TestFuturesCoin:
    def setup_class(self):
        secret = load_json_config(os.path.join(os.path.dirname(__file__), 'secret.json'))
        self.test_client = Client(**secret['binance-test'], testnet=True)

    def test_account_data(self):
        account = self.test_client.futures_coin_account()
        print(account)

    def test_balance(self):
        balance = self.test_client.futures_coin_account_balance()
        print(balance)

    def test_position_risk(self):
        position = self.test_client.futures_coin_position_information()
        print(position)

    def test_create_order(self):
        order_res = self.test_client.futures_coin_create_order(symbol='BTCUSD_210625',
                                                               type='MARKET',
                                                               positionSide='LONG',
                                                               side='BUY',
                                                               quantity=1)
        print(order_res)
