print("TSLA Mean Reversion Strategy Output: 2024 – 2025 Data")

# Open and read file
file = open("/workspaces/Data_3500_Programming_Activities/HW4/TSLA.txt")
lines = file.readlines()

# Print each price value rounded to two decimals (your requested code)
for line in lines:
    price = float(line)
    price = round(price, 2)
    print(price)

# Build list of floats
def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

prices = [float(line.strip()) for line in lines if is_float(line.strip())]

final_profit = 0
first_buy = None
buy_price = None
trade_profits = []

for i in range(5, len(prices)):
    current_price = prices[i]
    avg_price = sum(prices[i-5:i]) / 5
    if current_price < avg_price * 0.98:
        if buy_price is None:
            buy_price = current_price
            if first_buy is None:
                first_buy = buy_price
            print(f"buying at:     {buy_price:.2f}")
    elif current_price > avg_price * 1.02 and buy_price is not None:
        profit = round(current_price - buy_price, 2)
        final_profit += profit
        trade_profits.append(profit)
        print(f"selling at:    {current_price:.2f}")
        print(f"trade profit:  {profit:.2f}")
        buy_price = None

if first_buy:
    final_profit_percentage = (final_profit / first_buy) * 100
else:
    final_profit_percentage = 0

print(f"\nTotal profit:  {final_profit:.2f}")
print(f"First buy:     {first_buy:.2f}")
print(f"% return:      {final_profit_percentage:.1f}")

# Close the file (best practice)
file.close()


