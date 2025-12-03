#Funtion definition
def apply_discount(prices):
    prices_copy = product_prices.copy()
    for cost in range(len(prices_copy)):
        if cost >= 2.00:
            discount_cost = cost * .10
            prices_copy.append(cost)
    return(prices_copy)    
    
# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print(f"Updated product prices:${updated_prices}")