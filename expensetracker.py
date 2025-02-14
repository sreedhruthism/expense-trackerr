import csv
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Function to initialize the CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

# Function to add an expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Transport, Entertainment, etc.): ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!\n")

# Function to view expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        expenses = list(reader)
        
        if not expenses:
            print("No expenses recorded yet.\n")
            return
        
        print("\nDate          | Category      | Description        | Amount")
        print("-" * 60)
        for row in expenses:
            print(f"{row[0]:<12} | {row[1]:<12} | {row[2]:<18} | ${row[3]:>5}")
        print()

# Function to generate reports
def generate_report():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return
    
    category_totals = {}
    monthly_totals = {}
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date, category, _, amount = row
            amount = float(amount)
            month = date[:7]  # Extract YYYY-MM for monthly summary
            
            category_totals[category] = category_totals.get(category, 0) + amount
            monthly_totals[month] = monthly_totals.get(month, 0) + amount
    
    print("\nCategory-wise Expenses:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
    
    print("\nMonthly Expenses:")
    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")
    print()

# Main menu function
def main():
    initialize_csv()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
