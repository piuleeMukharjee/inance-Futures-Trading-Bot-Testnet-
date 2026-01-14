import os
import logging
from binance import Client
from dotenv import load_dotenv

load_dotenv()

class TradingBot:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET")
        )

        # REAL TESTNET URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        logging.basicConfig(
            filename="bot.log",
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s"
        )

    def market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info(order)
            return order
        except Exception as e:
            logging.error(e)
            raise
