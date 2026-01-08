menu = {
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []

print("------ MENU ------")
for item, price in menu.items():
    print(f"{item:<10} : ${price:.2f}")
print("------------------")

# take all inputs first
while True:
    choice = input("Select an item (q to quit): ").lower()

    if choice == "q":
        break
    elif choice in menu:
        cart.append(choice)
    else:
        print("Item not available.")

# calculate total after all inputs
total = 0
for item in cart:
    total += menu[item]

# display result
print("\n------ YOUR ORDER ------")
for item in cart:
    print(item, end=" ")

print()
print(f"Total is: ${total:.2f}")