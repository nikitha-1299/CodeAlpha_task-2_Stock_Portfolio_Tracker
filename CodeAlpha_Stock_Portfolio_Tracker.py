# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

print("===== STOCK PORTFOLIO TRACKER =====")

total_investment = 0

while True:
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} - ${price}")

    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity

        print(f"Price per share: ${price}")
        print(f"Investment for {stock_name}: ${investment}")

        total_investment += investment

    except ValueError:
        print("❌ Please enter a valid quantity.")

print("\n===== PORTFOLIO SUMMARY =====")
print(f"Total Investment: ${total_investment}")

print("\nThank you for using Stock Portfolio Tracker!")
