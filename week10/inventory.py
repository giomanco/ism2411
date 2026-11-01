"""
Reflection:
1. The most surprising thing about how lists work in Python compared to what I expected was that indexing is very flexible. Python uses a negative index. This eliminates common errors that can otherwise require manaul checking.
2. From my Statistics II class, Python could have automated calculating information from a spreadsheet instead of having to manually write the formulas.
"""

# Exercise 1:
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2:
first_item = inventory[0]
last_item = inventory[-1]
middle_item = inventory[len(inventory) // 2]
print(f"{first_item} | {last_item} | {middle_item}")

# Exercise 3:
first_three = inventory[:3]
last_two = inventory[-2:]
every_other = inventory[::2]
print(first_three)
print(last_two)
print(every_other)

# Exercise 4:
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5:
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print(f"Caught error: {e}")
    print("Tuples are immutable, ensuring fixed reference points like coordinates cannot be accidentally altered.")
    print(coords)
# Exercise 6:
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)
print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_day} | Worst: {worst_day}")
# Exercise 7:
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print(f"Original: {prices}")
print(f"Discounted: {discounted}")
#Exercise 8:
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales_data:
    if sale > 300:
        high_sales.append(sale)
count_high = len(high_sales)
avg_high = sum(high_sales) / count_high
print(f"High Sales: {high_sales} | Count: {count_high} | Avg: {round(avg_high, 2)}")
