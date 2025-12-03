#Function definition with default values
def apply_discount(price, discount=0.05):
    discount_total = price * (1 - discount)
    return discount_total
def apply_tax(price, tax=0.07):
    tax_total = price * (1 + tax)
    return tax_total
def calculate_total(price, discount=0.05, tax=0.07):
    total_price = price * (1 + tax) * (1 - discount)
    return total_price
#Calling the function using keyword arguments
total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")

