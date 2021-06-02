import os

from binance.client import Client
from tests.utils import load_json_config


class TestMargin:
    def setup_class(self):
        secret = load_json_config(os.path.join(os.path.dirname(__file__), 'secret.json'))
        self.client = Client(**secret['fanyong'])

    # def test_transfer_dust(self):
    #     res = self.client.transfer_dust(asset=['BCH', 'BTC'])
    #     print(res)

    def test_dust(self):
        print(self.client.get_dust_log())
