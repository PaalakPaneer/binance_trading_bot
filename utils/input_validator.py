def validate_symbol(symbol: str) -> str:
    return symbol.upper()

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT or STOP_LIMIT")
    return order_type

def validate_quantity(qty: str) -> float:
    try:
        qty = float(qty)
        if qty <= 0:
            raise ValueError()
        return qty
    except:
        raise ValueError("Quantity must be a positive number")

def validate_price(price: str) -> float:
    try:
        price = float(price)
        if price <= 0:
            raise ValueError()
        return price
    except:
        raise ValueError("Price must be a positive number")
