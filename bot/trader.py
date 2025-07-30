from bot.client import get_binance_client
from bot.logger import setup_logger
from binance.exceptions import BinanceAPIException, BinanceOrderException
import time

class BasicBot:
    def __init__(self):
        self.client = get_binance_client()
        self.logger = setup_logger()

    def place_market_order(self, symbol, side, quantity):
        try:
            self.logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            self.logger.info(f"Order Response: {order}")
            return {
                "status": "success",
                "order": order
            }
        except (BinanceAPIException, BinanceOrderException) as e:
            self.logger.error(f"Error placing market order: {e}")
            return {"status": "error", "message": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            self.logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} @ {price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            self.logger.info(f"Order Response: {order}")
            return {
                "status": "success",
                "order": order
            }
        except (BinanceAPIException, BinanceOrderException) as e:
            self.logger.error(f"Error placing limit order: {e}")
            return {"status": "error", "message": str(e)}

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            self.logger.info(f"Placing STOP-LIMIT order: {side} {quantity} {symbol} STOP={stop_price}, LIMIT={limit_price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=stop_price,
                quantity=quantity,
                timeInForce="GTC",
                closePosition=False,
                price=limit_price
            )
            self.logger.info(f"Order Response: {order}")
            return {
                "status": "success",
                "order": order
            }
        except (BinanceAPIException, BinanceOrderException) as e:
            self.logger.error(f"Error placing stop-limit order: {e}")
            return {"status": "error", "message": str(e)}

    def wait_until_filled_or_cancel(self, symbol, order_id, timeout=60):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                order = self.client.futures_get_order(symbol=symbol, orderId=order_id)
                status = order.get("status")
                if status == "FILLED":
                    self.logger.info(f"Order {order_id} filled.")
                    return order
                elif status in ["CANCELED", "REJECTED", "EXPIRED"]:
                    self.logger.info(f"Order {order_id} is {status}.")
                    return order
                time.sleep(2)
            except Exception as e:
                self.logger.error(f"Error checking order status: {e}")
                break
        self.logger.warning(f"Timeout reached. Cancelling order {order_id}.")
        try:
            self.client.futures_cancel_order(symbol=symbol, orderId=order_id)
            self.logger.info(f"Order {order_id} canceled.")
        except Exception as e:
            self.logger.error(f"Failed to cancel order: {e}")
        return None

    def cancel_all_open_orders(self, symbol):
        try:
            self.logger.info(f"Cancelling all open orders for {symbol}")
            response = self.client.futures_cancel_all_open_orders(symbol=symbol.upper())
            self.logger.info(f"Cancel response: {response}")
            return {
                "status": "success",
                "response": response
            }
        except Exception as e:
            self.logger.error(f"Error cancelling orders for {symbol}: {e}")
            return {
                "status": "error",
                "message": str(e)
            }
        
    def get_open_orders(self, symbol):
        try:
            return self.client.futures_get_open_orders(symbol=symbol.upper())
        except Exception as e:
            self.logger.error(f"Error fetching open orders: {e}")
            return []

    def get_position_info(self, symbol):
        try:
            positions = self.client.futures_position_information(symbol=symbol.upper())
            return positions[0] if positions else {}
        except Exception as e:
            self.logger.error(f"Error fetching position info: {e}")
            return {}

    def get_wallet_balance(self):
        try:
            balances = self.client.futures_account_balance()
            usdt_balance = next((b for b in balances if b['asset'] == 'USDT'), None)
            return usdt_balance or {}
        except Exception as e:
            self.logger.error(f"Error fetching wallet balance: {e}")
            return {}
    def get_open_positions(self):
        try:
            account_info = self.client.futures_account()
            positions = account_info.get("positions", [])

            # Filter only positions with non-zero amount
            open_positions = [
                p for p in positions if float(p["positionAmt"]) != 0.0
            ]

            return open_positions
        except Exception as e:
            self.logger.error(f"Error fetching open positions: {e}")
            return []
