grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
#Check and update price
egg_price = grocery_inventory.get("Eggs")[1]
if egg_price > 5 :
    print("Eggs are too expensive, reducing the price by $1.")
    egg_price = egg_price - 1.00
    grocery_inventory.update({"Eggs": ("Dairy", egg_price, 30)})
    print("Eggs are now ", egg_price)
else :
    print("The price of Eggs is reasonable.")
#Add new item
new_item = {"Tomatoes": ("Produce", 1.20, 30)}
grocery_inventory.update(new_item)
print("Inventory after adding Tomatoes:", grocery_inventory)
#Manage stock
milk_stock = grocery_inventory.get("Milk")[2]
if milk_stock < 10 :
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    milk_stock = milk_stock + 20
    grocery_inventory.update({"Milk": ("Dairy", 3.50, milk_stock)})
#Remove item based on price
apple_price = grocery_inventory.get("Apples")[1]
if apple_price > 2.00 :
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
#Final print
print("Updated inventory: ", grocery_inventory)