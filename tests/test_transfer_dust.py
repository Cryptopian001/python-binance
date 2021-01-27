import json
import os

from binance.client import Client


def load_json_config(json_config_file_path: str, encoding: str = 'utf-8') -> dict:
    with open(json_config_file_path, encoding=encoding) as f:
        return json.load(f)


class TestMargin:
    def setup_class(self):
        secret = load_json_config(os.path.join(os.path.dirname(__file__), 'secret.json'))
        self.client = Client(**secret['fanyong'])

    def test_transfer_dust(self):
        res = self.client.transfer_dust(asset=['BCH', 'BTC'])
        print(res)
