#using list , set , tuples to manage a shopping cart
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item to add to buy (or 'q' to quit) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food} : "))
        foods.append(food)
        prices.append(price)

print("\n----- YOUR CART -----")

for i in range(len(foods)):
    print(f"{foods[i]} : ${prices[i]}")

total = sum(prices)
print(f"\nYour total is ${total}")