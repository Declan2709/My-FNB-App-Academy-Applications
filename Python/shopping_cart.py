#A shopping cart that allows adding, removing, and viewing items.

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy or press q to quit: ")
    if food.lower() == 'q':
        break 
    else:
        price = float(input("Enter price of {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("------ YOUR CART ---")

for food in food:
    print(food, end= " ")
    
for price in prices:
    total += price

print("\n")
print(f"Your total is: R{total}")