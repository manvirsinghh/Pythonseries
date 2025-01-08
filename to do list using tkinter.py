import tkinter as tk

# Function to add a task to the list
def add_task():
    task = task_entry.get()  # Get the task from the entry widget
    if task != "":  # Check if the task is not empty
        task_listbox.insert(tk.END, task)  # Add task to the listbox
        task_entry.delete(0, tk.END)  # Clear the entry field after adding the task

# Function to delete a selected task from the list
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get selected task index
        task_listbox.delete(selected_task_index)  # Delete the selected task
    except IndexError:
        pass  # If no task is selected, do nothing

# Function to mark the selected task as completed (strike-through)
def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get selected task index
        task = task_listbox.get(selected_task_index)  # Get the task text
        task_listbox.delete(selected_task_index)  # Remove the task
        task_listbox.insert(selected_task_index, f"{task} - Completed")  # Reinsert it with 'Completed' text
    except IndexError:
        pass  # If no task is selected, do nothing

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Create a label to display the title of the application
title_label = tk.Label(root, text="To-Do List", font=("Arial", 16))
title_label.pack(pady=10)

# Create an entry widget to input a new task
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Create a button to add the task
add_button = tk.Button(root, text="Add Task", font=("Arial", 14), command=add_task)
add_button.pack(pady=5)

# Create a listbox to display the tasks
task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# Create a button to delete the selected task
delete_button = tk.Button(root, text="Delete Task", font=("Arial", 14), command=delete_task)
delete_button.pack(pady=5)

# Create a button to mark the selected task as completed
complete_button = tk.Button(root, text="Mark as Completed", font=("Arial", 14), command=complete_task)
complete_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
