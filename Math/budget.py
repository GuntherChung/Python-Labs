import pandas as pd
class Bill:
    def __init__(self, name, amount, due_date):
        self.name = name
        self.amount = amount
        self.due_date = due_date

def capture_income():
    while True:
        try:
            income = float(input("Enter your monthly income: "))
            return income
        except ValueError:
            print("Please enter a valid number.")

def capture_bill():
    name = input("Enter the bill name: ")
    while True:
        try:
            amount = float(input("Enter the bill amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    due_date = input("Enter the bill due date (e.g., 2024-08-01): ")
    return Bill(name, amount, due_date)

def main():
    income = capture_income()
    bills = []
    allocation = {}

    while True:
        add_bill = input("Do you want to add a bill? (yes/no): ").strip().lower()
        if add_bill == 'yes':
            bill = capture_bill()
            bills.append(bill)
        elif add_bill == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")

    for bill in bills:
        while True:
            try:
                percentage = float(input(f"Enter the percentage of income to allocate for {bill.name}: "))
                if 0 <= percentage <= 100:
                    allocation[bill.name] = (percentage / 100) * income
                    break
                else:
                    print("Please enter a percentage between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    print("\nSummary of Bill Allocations:")
    for bill in bills:
        allocated_amount = allocation[bill.name]
        print(f"Bill: {bill.name}, Amount: {bill.amount}, Due Date: {bill.due_date}, Allocated Amount: {allocated_amount:.2f}")

if __name__ == "__main__":
    main()