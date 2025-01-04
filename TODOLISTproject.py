# To-Do List PROJECT  using Python

tasks = []  # List to store tasks

def add_task(task):
    if task not in tasks:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print(f"Task '{task}' is already present in the list.")

def view_task():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("Here are the tasks in your list:")
        task_number = 1
        for task in tasks:
            print(f"Task {task_number}: {task}")
            task_number += 1

def delete_task(task_number):
    try:
        # Adjusting for 0-based index by subtracting 1
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted successfully.")
    except IndexError:
        print("Invalid task number. Task not found.")

# Main program loop
print("Welcome to the To-Do List program:")

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit the program")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue  # Skip to the next iteration of the loop

    if choice == 1:
        task = input("Enter the task to add: ")
        add_task(task)

    elif choice == 2:
        view_task()

    elif choice == 3:
        view_task()  # Show tasks first, so the user can pick one to delete
        try:
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        except ValueError:
            print("Please enter a valid task number.")

    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Please enter a valid choice (1-4).")