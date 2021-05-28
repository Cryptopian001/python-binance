import json
import os

from binance.client import Client


def load_json_config(json_config_file_path: str, encoding: str = 'utf-8') -> dict:
    with open(json_config_file_path, encoding=encoding) as f:
        return json.load(f)


class TestDelivery:
    def setup_class(self):
        secret = load_json_config(os.path.join(os.path.dirname(__file__), 'secret.json'))
        self.test_client = Client(**secret['binance-test'], test=True)

    def test_account_data(self):
        account = self.test_client.delivery_account()
        print(account)

    def test_balance(self):
        balance = self.test_client.delivery_account_balance()
        print(balance)

    def test_position_risk(self):
        position = self.test_client.delivery_position_information()
        print(position)

    def test_create_trade(self):
        order_res = self.test_client.delivery_create_order(symbol='BTCUSD_210625',
                                                           type='MARKET',
                                                           positionSide='LONG',
                                                           side='BUY',
                                                           quantity=1)
        print(order_res)
