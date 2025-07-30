from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL

def get_binance_client():
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = BASE_URL + "/fapi"
    client.FUTURES_ACCOUNT_URL = BASE_URL
    return client
