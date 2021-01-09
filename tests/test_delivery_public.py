from binance.client import Client


class TestDeliveryPublic:
    def setup_class(self):
        self.client = Client()

    def test_symbol_ticker(self):
        symbol_tickers = self.client.delivery_symbol_ticker()
        print(symbol_tickers)
