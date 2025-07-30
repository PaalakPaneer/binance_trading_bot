Binance Futures Testnet Trading Bot
A command-line trading bot for Binance Futures Testnet built with Python.
Supports placing and managing Market, Limit, and Stop-Limit orders, tracking wallet balance, viewing open positions, and canceling open orders — all via an interactive menu.

Features
Place Market, Limit, and Stop-Limit orders

Cancel all open orders by symbol

View current wallet balance

See open positions on the Futures Testnet

Works non-blocking: place new orders while old ones fill

Modular and extensible design

Folder Structure
[CODE START]text
binance_trading_bot/
├── bot/
│ ├── trader.py
│ ├── client.py
│ └── logger.py
├── cli/
│ └── run.py
├── utils/
│ └── input_validator.py
├── config.py
├── requirements.txt
└── README.md
[CODE END]

Setup
Clone the repo
[CODE START]bash
git clone https://github.com/your-username/binance-trading-bot.git
cd binance-trading-bot
[CODE END]

(Optional) Create a virtual environment
[CODE START]bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
[CODE END]

Install dependencies
[CODE START]bash
pip install -r requirements.txt
[CODE END]

Add your Binance Testnet API keys
Create a file named config.py in the root directory:
[CODE START]python
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_secret_key"
BASE_URL = "https://testnet.binancefuture.com"
[CODE END]

Make sure you're using keys from https://testnet.binancefuture.com

Running the Bot
[CODE START]bash
python -m cli.run
[CODE END]

Example Actions
View Wallet Balance

View Open Positions

Place Order (Market, Limit, Stop-Limit)

Cancel All Open Orders