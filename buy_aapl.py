from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = "PKQYQWIKFWD362CPIWZKPOWGS3"
API_SECRET = "4GUZowdzUNUFFrQxfG7oFwVBtsnF6XQhXmPnKfgrfN4A"

client = TradingClient(API_KEY, API_SECRET, paper=True)

# Verify connection
account = client.get_account()
print(f"Account status: {account.status}")
print(f"Buying power: ${float(account.buying_power):,.2f}")

# Place market order for 1 share of AAPL
order_request = MarketOrderRequest(
    symbol="AAPL",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY,
)

order = client.submit_order(order_request)
print(f"\nOrder placed successfully!")
print(f"Order ID:  {order.id}")
print(f"Symbol:    {order.symbol}")
print(f"Qty:       {order.qty}")
print(f"Side:      {order.side}")
print(f"Type:      {order.order_type}")
print(f"Status:    {order.status}")
