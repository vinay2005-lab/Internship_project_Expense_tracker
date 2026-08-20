
---

## 📄 PROJECT_REPORT.md

```markdown
# Project Report: Personal Expense Manager

## 1. Problem Understanding
Managing personal expenses manually often leads to errors and lack of clarity. A simple digital tracker can help users record, categorize, and analyze their financial transactions.

## 2. Proposed Approach
- Build a modular Python application.
- Use JSON for local data persistence.
- Provide a CLI menu for user interaction.
- Implement core features: add, view, search, delete, and summary.
- Ensure test coverage with meaningful cases.

## 3. Implementation
- **storage.py**: Handles reading/writing JSON files.
- **expense_manager.py**: Contains `ExpenseManager` class with methods for adding, viewing, searching, deleting, and summarizing transactions.
- **main.py**: CLI menu system for user interaction.
- **tests/test_expense_tracker.py**: Unit tests covering normal, invalid, and boundary cases.

## 4. Important Technical Decisions
- **JSON storage** chosen for simplicity and persistence.
- **Object-Oriented Design** with `ExpenseManager` class for modularity.
- **CLI interface** for quick implementation within time constraints.

## 5. Testing Performed
- Added income and expense transactions.
- Verified summary calculations.
- Tested search by category.
- Tested deletion of transactions.
- Handled invalid transaction type input.

## 6. Challenges Encountered
- Ensuring persistence across sessions.
- Validating transaction type input.
- Designing a simple yet extensible structure.

## 7. Solutions Implemented
- Used JSON file for persistence.
- Added input validation for transaction type.
- Modularized code into separate files for clarity.

## 8. Future Scope
- Implement GUI for better usability.
- Add advanced filtering (date range, amount range).
- Switch to SQLite for scalability.
- Add visualization (pie charts, bar graphs) for category-wise spending.

---
