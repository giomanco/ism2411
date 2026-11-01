# Self-Assessment Questions:
# 1. The first bug I spotted in Exercise 5 was that the total was being set to the current sale instead of accumulating the total. I found it from explaining the code out loud to the duck. I realized that the total should be accumulating the sales, not just taking the last sale value. This tells me that my debugging skills are sharp. 
# 2. 'apply_discount(price, tier) is a function that takes a price and a tier (like 'gold', 'silver', or 'bronze') and returns the price after applying the appropriate discount based on the tier. The function checks the tier and applies a 15% discount for gold, a 5% discount for silver, and no discount for bronze or any other tier. Yes, a colleague could use it without reading the body because the return clearly shows the discounted price based on the tier.
# 3. AI Disclosure: AI was used to help me understand the code and identify bugs. I used it to explain the purpose of functions and to clarify the logic behind the discount application. It helped me think through the problems and provided insights that I might have missed on my own. The AI use helps me understand how to properly debug, ultimately improving my coding skills and ensuring that I can write more efficient and error-free code in the future.

# Exercise 1:
def calculate_tax(price, tax_rate):
    return price * tax_rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# Exercise 2:
def apply_discount(price, tier):
    if tier == "gold":
        return price * (1-0.15)
    elif tier == "silver":
        return price * (1-0.05)
    else:
        return price
for t in ["gold", "silver", "bronze", "none"]:
    print(f"{t:7}: ${apply_discount(200, t):.2f}")

# Exercise 3:
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
total = discounted + tax
print(f"After gold discount: ${discounted:.2f}, After tax: ${total:.2f}")
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount
print(f"final_price(200, 'gold', 0.07): ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4:
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 5:
# Bug 1: 'total = sale' should be 'total += sale'
# Bug 2: Missing colon after 'for sale in sales'; fixed by adding ':'.
# Bug 3: The while loop condition should be 'i < len(sales)' to avoid IndexError; fixed by changing '<=' to '<'.
sales = [120, 80, 250, 175, 90]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")
i = 0
while i < len(sales):
    print(sales[i])
    i += 1
# Exercise 6:
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # prints 100
print(double_it()) # prints 1998
print(x)           # still prints 100
# Scope Explanation: The variable x inside the function double_it is a local variable and does not affect the global variable x.
