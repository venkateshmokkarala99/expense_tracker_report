"""
Project_1 =  PERSONAL EXPENSE TACKER

"""
import csv
import os
from datetime import date

# ── File where all expenses are saved

FILENAME = "expenses.csv"

#1.	Create the CSV file with headers if it does not exist 
def setup_file():
    if  not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline ="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Description","Category","Amount"])
        print(f"created new file : {FILENAME}")





#2.	Add a new expense 
def add_expense(description, category, amount):
    if amount<=0:
        print("amount must be greater than zero")
        return
    today = date.today().strftime("%d-%m-%Y")
    with open(FILENAME, "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([today, description, category, amount])
    print(f"expenses added: {description} | {category} | Rs.{amount:.2f}")


#3.	Read all expenses from the file
def load_expenses():
    expenses = [] 
    with open(FILENAME, "r", newline = "") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Amount"]=float(row["Amount"])
            expenses.append(row)
    return expenses

#4.	Display all expenses
def show_all_expenses(expenses):
    if not expenses:
        print("expenses not recorded.")
        return
    print("-"*80)
    print(f"{'date':<12}{'description':<18}{'category':<10}{'amount':>8}")
    print("-"*80)

    for expense in expenses:
        print(
              f"{expense['Date']:<12}"
              f"{expense['Description']:<18}"
              f"{expense['Category']:<10}"
              f"{expense['Amount']:>6.2f}"
              )
    print("-"*80)

#5.	Show a summary by category# 
def show_summary(expenses):
    print("showing the summary of expenses.")
    if not expenses:
        print("no summary for this records.")
        return
    print("-"*80)
    category_totals = {}
    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]
        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category] = amount
    for category, total in category_totals.items():
        print(f"{category:<15}Rs.{total:>7.2f}")
    grand_total = sum(category_totals.values())
    print("-"*80)
    print(f"{'total':<15}{grand_total:>7.2f}")
    print("-"*80)




 
#6.	Show the most expensive item 
def highest_expense(expenses):
    if not expenses:
        print("no expenses recorded")
        return
    highest_expense=expenses[0]
    for expense in expenses:
        if expense['Amount']>highest_expense['Amount']:
            highest_expense=expense
    print(f"{'highest_expense:'}{highest_expense['Description']} is {highest_expense['Amount']:.2f}")
    print("*"*80)


def main():
    setup_file()

    # Adding sample expenses 
    add_expense("Groceries",      "Food",    850.00)
    add_expense("Bus pass",       "Travel",  500.00)
    add_expense("Electricity bill","Bills",  1200.00)
    add_expense("Lunch",          "Food",    180.00)
    add_expense("Notebook",       "Study",   120.00)
    add_expense("Auto ride",      "Travel",   90.00)
    add_expense("Internet bill",  "Bills",   699.00)
    add_expense("Coffee",         "Food",     60.00)

    # Loading expenses into expenses
    expenses = load_expenses()

    # Display results
    print("\nAll Expenses")
    show_all_expenses(expenses)
    show_summary(expenses)
    highest_expense(expenses)


if __name__ == "__main__":
    main()