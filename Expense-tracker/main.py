from expense_manager import ExpenseManager

def main():
    manager = ExpenseManager()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Summary")
        print("4. Search by Category")
        print("5. Delete Transaction")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                description = input("Description: ")
                t_type = input("Type (income/expense): ")
                manager.add_transaction(amount, category, description, t_type)
                print("Transaction added successfully!")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            manager.view_transactions()
        elif choice == "3":
            print(manager.summary())
        elif choice == "4":
            category = input("Enter category: ")
            results = manager.search_by_category(category)
            print(results if results else "No transactions found.")
        elif choice == "5":
            try:
                tid = int(input("Enter transaction ID to delete: "))
                manager.delete_transaction(tid)
                print("Transaction deleted.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
