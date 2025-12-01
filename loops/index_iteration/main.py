prices = [29.99, 45.50, 12.75, 38.20]
for value in range(len(prices)):
    if value == 0:
       prices[value] -= prices[value] * .10
       print(f"Updated price for item {value + 1}: ${prices[value]:.2f}")
    elif value == 1:
       prices[value] -= prices[value] * .20
       print(f"Updated price for item {value + 1}: ${prices[value]:.2f}")
    elif value == 2:
       prices[value] -= prices[value] * .15
       print(f"Updated price for item {value + 1}: ${prices[value]:.2f}")
    elif value == 3:
       prices[value] -= prices[value] * .05
       print(f"Updated price for item {value + 1}: ${prices[value]:.2f}")
          