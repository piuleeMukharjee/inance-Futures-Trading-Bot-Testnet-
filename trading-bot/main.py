from bot import TradingBot

bot = TradingBot()

symbol = input("Symbol (BTCUSDT): ").upper()
side = input("BUY or SELL: ").upper()
qty = float(input("Quantity: "))

result = bot.market_order(symbol, side, qty)

print("Order Placed Successfully")
print("Order ID:", result.get("orderId", "N/A"))
print("Client Order ID:", result.get("clientOrderId", "N/A"))
print("Status:", result.get("status", "N/A"))
print("Executed Qty:", result.get("executedQty", "N/A"))
print("Average Price:", result.get("avgPrice", "N/A"))

