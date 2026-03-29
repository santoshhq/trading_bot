from binance.client import Client
import os
from dotenv import load_dotenv
load_dotenv()
def get_client():
    return Client(
        api_key=os.getenv("API_KEY"),
        api_secret=os.getenv("SECRET_KEY"),
        testnet=True
    )