from binance.client import Client


class TestFuturesCoinPublic:
    def setup_class(self):
        self.client = Client()

    def test_symbol_ticker(self):
        symbol_tickers = self.client.futures_coin_symbol_ticker()
        print(symbol_tickers)
