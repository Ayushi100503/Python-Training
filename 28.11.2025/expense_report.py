write_line = lambda item, amount: f"{item}:Rs{amount}\n"

def write_expense_report(expenses):
    total = sum(amount for item, amount in expenses)

    with open("report.txt", "w") as file:
        file.write("Expense Report\n")
        for item, amount in expenses:
            file.write(write_line(item, amount))
        file.write("\n")
        file.write(f"Total: {total}\n")

expenses = [("Food", 200), ("Travel", 800), ("Books", 500), ("Shopping", 600)]
write_expense_report(expenses)
print("expenses report created successfully")