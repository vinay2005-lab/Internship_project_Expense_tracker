from storage import load_data, save_data
from datetime import datetime

class ExpenseManager:
    def __init__(self):
        self.transactions = load_data()

    def add_transaction(self, amount, category, description, t_type):
        if t_type not in ["income", "expense"]:
            raise ValueError("Transaction type must be 'income' or 'expense'")
        transaction = {
            "id": len(self.transactions) + 1,
            "type": t_type,
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)
        save_data(self.transactions)

    def view_transactions(self):
        for t in self.transactions:
            print(t)

    def summary(self):
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expenses = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        balance = income - expenses
        return {"income": income, "expenses": expenses, "balance": balance}

    def search_by_category(self, category):
        return [t for t in self.transactions if t["category"].lower() == category.lower()]

    def delete_transaction(self, transaction_id):
        self.transactions = [t for t in self.transactions if t["id"] != transaction_id]
        save_data(self.transactions)
