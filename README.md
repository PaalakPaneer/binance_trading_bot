# Binance Futures Testnet Trading Bot

A command-line trading bot for Binance Futures Testnet built with Python.
Supports placing and managing Market, Limit, and Stop-Limit orders, tracking wallet balance, viewing open positions, and canceling open orders — all via an interactive menu.

# Features

Place Market, Limit, and Stop-Limit orders

Cancel all open orders by symbol

View current wallet balance

See open positions on the Futures Testnet

Works non-blocking: place new orders while old ones fill

Modular and extensible design

# Setup

Clone the repo
```
git clone https://github.com/your-username/binance-trading-bot.git
cd binance-trading-bot
```

Install dependencies
```
pip install -r requirements.txt
```

Add your Binance Testnet API keys
Create a file named config.py in the root directory:
```
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_secret_key"
BASE_URL = "https://testnet.binancefuture.com"
```

Make sure you're using keys from https://testnet.binancefuture.com

Running the Bot
```
python -m cli.run
```

# Example Actions
View Wallet Balance

View Open Positions

Place Order (Market, Limit, Stop-Limit)

Cancel All Open Orders