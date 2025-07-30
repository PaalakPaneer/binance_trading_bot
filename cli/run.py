from bot.trader import BasicBot
from utils.input_validator import (
    validate_symbol, validate_side, validate_order_type,
    validate_quantity, validate_price
)
import questionary


def place_order(bot):
    symbol = validate_symbol(
        questionary.text("Symbol", default="BTCUSDT").ask()
    )

    side = validate_side(
        questionary.select("Side", choices=["BUY", "SELL"]).ask()
    )

    order_type = validate_order_type(
        questionary.select("Order Type", choices=["MARKET", "LIMIT", "STOP_LIMIT"]).ask()
    )

    quantity = validate_quantity(
        questionary.text("Quantity").ask()
    )

    if order_type == "LIMIT":
        price = validate_price(questionary.text("Limit Price").ask())
        result = bot.place_limit_order(symbol, side, quantity, price)

    elif order_type == "STOP_LIMIT":
        stop_price = validate_price(questionary.text("Stop Price").ask())
        limit_price = validate_price(questionary.text("Limit Price").ask())
        result = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)

    else:
        result = bot.place_market_order(symbol, side, quantity)

    if result["status"] == "success":
        order = result["order"]
        order_id = order.get("orderId")

        print("\nOrder placed successfully!")
        print(f"Order ID     : {order_id}")
        print(f"Status       : {order.get('status')}")

        if questionary.confirm("Wait for order to fill (auto-cancel after 15s)?").ask():
            bot.wait_until_filled_or_cancel(symbol, order_id)

        if questionary.confirm("View open orders for this symbol?").ask():
            open_orders = bot.get_open_orders(symbol)
            if open_orders:
                print("\nOpen Orders:")
                for o in open_orders:
                    print(f"- Order ID: {o['orderId']}, Type: {o['type']}, Status: {o['status']}, Qty: {o['origQty']}, Filled: {o['executedQty']}")
            else:
                print("No open orders.")
    else:
        print(f"Order failed: {result['message']}")


def main():
    bot = BasicBot()
    print("Binance Futures Testnet Trading Bot")

    while True:
        action = questionary.select(
            "Choose an action",
            choices=[
                "Place Order",
                "View Wallet Balance",
                "Cancel All Open Orders",
                "View Open Positions",
                "Exit"
            ]
        ).ask()

        if action == "Place Order":
            place_order(bot)

        elif action == "View Wallet Balance":
            balance = bot.get_wallet_balance()
            print("\nWallet Balance:")
            for asset, amount in balance.items():
                print(f"{asset}: {amount}")

        elif action == "Cancel All Open Orders":
            symbol = validate_symbol(questionary.text("Symbol to cancel orders for").ask())
            result = bot.cancel_all_open_orders(symbol)
            if result["status"] == "success":
                print("All open orders canceled.")
            else:
                print(f"Failed to cancel orders: {result['message']}")

        elif action == "View Open Positions":
            positions = bot.get_open_positions()
            if positions:
                print("\nOpen Positions:")
                for pos in positions:
                    print(f"{pos['symbol']} - {pos['positionSide']}, Qty: {pos['positionAmt']}, Entry Price: {pos['entryPrice']}")
            else:
                print("No open positions.")

        elif action == "Exit":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
