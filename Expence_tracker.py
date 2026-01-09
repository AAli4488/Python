# Expense Tracker System in Python

expenses = []

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Study/etc): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    print("✅ Expense added successfully!")

def view_expenses():
    if not expenses:
        print("❌ No expenses found.")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Date: {exp['date']} | Category: {exp['category']} | "
              f"Amount: ₹{exp['amount']} | Description: {exp['description']}")

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print("💰 Total Expense: ₹", total)

def filter_by_category():
    cat = input("Enter category to filter: ")
    found = False

    print(f"\n--- Expenses in {cat} Category ---")
    for exp in expenses:
        if exp["category"].lower() == cat.lower():
            print(f"Date: {exp['date']} | Amount: ₹{exp['amount']} | "
                  f"Description: {exp['description']}")
            found = True

    if not found:
        print("❌ No expenses found in this category.")

# Main Menu
while True:
    print("\n--- EXPENSE TRACKER MENU ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Filter by Category")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        filter_by_category()
    elif choice == "5":
        print("👋 Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Try again.")