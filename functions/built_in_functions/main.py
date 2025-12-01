# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for items in products:
    product_name = items
    price = float(products[items][0])
    quantity = int(products[items][1])
    total_sales = price * quantity
    print(f"Total sales for {items}: ${total_sales:.2f}")
    total_sales_list.append(total_sales)
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Total sum of all sales: ${total_sum:.2f}")
print(f"Minimum sales: ${min_sales:.2f}")
print(f"Maximum sales: ${max_sales:.2f}")
