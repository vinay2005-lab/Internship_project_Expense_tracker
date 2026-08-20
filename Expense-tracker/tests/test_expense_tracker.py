import unittest
from expense_manager import ExpenseManager

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.manager = ExpenseManager()

    def test_add_income(self):
        self.manager.add_transaction(1000, "Salary", "Monthly pay", "income")
        self.assertTrue(any(t["category"] == "Salary" for t in self.manager.transactions))

    def test_add_expense(self):
        self.manager.add_transaction(200, "Food", "Dinner", "expense")
        self.assertTrue(any(t["category"] == "Food" for t in self.manager.transactions))

    def test_summary(self):
        self.manager.add_transaction(1000, "Salary", "Monthly pay", "income")
        self.manager.add_transaction(200, "Food", "Dinner", "expense")
        summary = self.manager.summary()
        self.assertEqual(summary["income"], 1000)
        self.assertEqual(summary["expenses"], 200)
        self.assertEqual(summary["balance"], 800)

    def test_search_category(self):
        self.manager.add_transaction(300, "Transport", "Bus fare", "expense")
        results = self.manager.search_by_category("Transport")
        self.assertTrue(len(results) > 0)

    def test_delete_transaction(self):
        self.manager.add_transaction(500, "Gift", "Birthday gift", "expense")
        tid = self.manager.transactions[-1]["id"]
        self.manager.delete_transaction(tid)
        self.assertFalse(any(t["id"] == tid for t in self.manager.transactions))

if __name__ == "__main__":
    unittest.main()
