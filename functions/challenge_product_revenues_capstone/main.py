# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
#Create tuple
grocery_list = (products,prices,quantities_sold)
item_catalog = []
for item in range(len(products)):
    item_catalog += [l[i] for l in grocery_list] 
print(item_catalog)
#Calculate total revenue for each products
#def calculate_revenue(prices, quantities_sold):
    
#Sort alphabetically and display the results
#def formatted_output(revenues):
    

# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")