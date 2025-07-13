from db import create_connection, insert_expense, fetch_expenses

def menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Enter description: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            insert_expense(desc, amount, date)
        elif choice == "2":
            expenses = fetch_expenses()
            for exp in expenses:
                print(f"{exp[0]} | {exp[1]} | ₹{exp[2]} | {exp[3]}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    create_connection()
    menu()