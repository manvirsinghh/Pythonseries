import tkinter as tk

# Function to update the display (Entry widget)
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())  # Use eval to evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")

# Create an entry widget to display the input and result
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="center")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout (text, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0),
]

# Create buttons and place them in the grid
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),command=clear)
    elif text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the Tkinter main loop
root.mainloop()
