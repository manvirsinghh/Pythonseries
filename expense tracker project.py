def add_expenses():
    with open("expenses.txt", "a") as file:
        date = input("Enter the date (yyyy-mm-dd): ")
        description = input("Enter the description: ")
        while True:
            try:
                amount = float(input("Enter the amount: "))
                break  # Exit loop if the input is valid
            except ValueError:
                print("Invalid input. Please enter a valid number for the amount.")
        file.write(f"{date},{description},{amount}\n")
        print("Expense added successfully.")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date, description, amount = line.strip().split(",")
                print(f"{date} - {description}: {amount}")
    except FileNotFoundError:
        print("No expense records found. Please add expenses first.")

def calculate_total():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                _, _, amount = line.strip().split(",")  # We don't need the date and description here
                total += float(amount)
        print(f"Total expenditure: {total}")
    except FileNotFoundError:
        print("No expense records found. Please add expenses first.")
    except ValueError:
        print("Error reading expense data. Please ensure the file format is correct.")

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total expenses")
    print("4. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_expenses()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            calculate_total()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a correct option.")
    
    except ValueError:
        print("Invalid input. Please enter a number for the choice.")
