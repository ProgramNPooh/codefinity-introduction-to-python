#Funtion definition
def apply_discount(prices):
    prices_copy = prices.copy()             # use the parameter
    for price_index in range(len(prices_copy)):       
        price = prices_copy[price_index]
        if price > 2.00:
            disc_cost = price * 0.90          # apply 10% discount
            prices_copy[price_index] = disc_cost
    return prices_copy  
    
# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(f"Updated product prices:${updated_prices}")