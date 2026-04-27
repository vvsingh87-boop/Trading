import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()

def get_trading_client(paper: bool = True) -> TradingClient:
    api_key = os.getenv("ALPACA_API_KEY")
    api_secret = os.getenv("ALPACA_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("ALPACA_API_KEY and ALPACA_API_SECRET must be set in environment or .env file")

    return TradingClient(api_key, api_secret, paper=paper)
