import tkinter as tk
from tkinter import ttk

# Function for length conversions
def convert_length(type):
    """
    Converts length units based on the selected type.
    
    Parameters:
    type (str): The type of conversion to perform.
    
    Returns:
    None
    """
    try:
        value = entry.get()
        if not value:
            result_string.set("Please enter a value")
            return
        
        value = float(value)
        
        if type == '1. Meter to kilometers':
            result_string.set(f"{value} meter is equal to: {value / 1000} kilometers")
        elif type == '2. Kilometers to meters':
            result_string.set(f"{value} kilometer is equal to: {value * 1000} meters")
        elif type == '3. Miles to kilometers':
            result_string.set(f"{value} miles is equal to: {value * 1.609} kilometers")
        elif type == '4. Kilometers to miles':
            result_string.set(f"{value} kilometer is equal to: {0.62137119 * value} miles")
    except ValueError:
        result_string.set("Invalid input. Please enter a number.")

# Function for temperature conversions
def convert_temperature(type):
    """
    Converts temperature units based on the selected type.
    
    Parameters:
    type (str): The type of conversion to perform.
    
    Returns:
    None
    """
    try:
        value = entry.get()
        if not value:
            result_string.set("Please enter a value")
            return
        
        value = float(value)
        
        if type == '1. Celsius to Fahrenheit':
            result_string.set(f"{value} Celsius is equal to: {(9/5)*value + 32} Fahrenheit")
        elif type == '2. Fahrenheit to Celsius':
            result_string.set(f"{value} Fahrenheit is equal to: {(5/9)*(value - 32)} Celsius")
        elif type == '3. Celsius to Kelvin':
            result_string.set(f"{value} Celsius is equal to: {value + 273.15} Kelvin")
        elif type == '4. Fahrenheit to Kelvin':
            result_string.set(f"{value} Fahrenheit is equal to: {((value - 32) * 5/9) + 273.15} Kelvin")
    except ValueError:
        result_string.set("Invalid input. Please enter a number.")

# Create a window
window = tk.Tk()
window.title("Unit Converter")
window.geometry("400x400")
window.configure(bg='lightblue')

# ttk label
label = ttk.Label(master=window, text="Welcome to\nUnit Converter", justify='center', font=('caliber', 24, 'bold'), background='lightblue')
label.pack(pady=20)

items = ('1. Length Conversion', '2. Temperature Conversion')
conversion_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, values=items, textvariable=conversion_string, width=30)
combo.pack(pady=10)

from_to_items = [
    ('1. Meter to kilometers', '2. Kilometers to meters', '3. Miles to kilometers', '4. Kilometers to miles'),
    ('1. Celsius to Fahrenheit', '2. Fahrenheit to Celsius', '3. Celsius to Kelvin', '4. Fahrenheit to Kelvin')
]
from_to_string = tk.StringVar(value=from_to_items[0][0])
from_to_combo = ttk.Combobox(window, values=from_to_items[0], textvariable=from_to_string, width=30)
from_to_combo.pack(pady=10)

def update_from_to_combo(event):
    """
    Updates the 'from_to_combo' values based on the selected conversion type.
    
    Parameters:
    event: The event that triggered the function.
    
    Returns:
    None
    """
    if conversion_string.get() == '1. Length Conversion':
        from_to_combo['values'] = from_to_items[0]
        from_to_string.set(from_to_items[0][0])
    else:
        from_to_combo['values'] = from_to_items[1]
        from_to_string.set(from_to_items[1][0])

def choose():
    """
    Chooses the appropriate conversion function based on the selected conversion type.
    
    Returns:
    None
    """
    value = from_to_string.get()
    if conversion_string.get() == '1. Length Conversion':
        convert_length(value)
    elif conversion_string.get() == '2. Temperature Conversion':
        convert_temperature(value)

# Events
combo.bind('<<ComboboxSelected>>', update_from_to_combo)

entry = ttk.Entry(master=window, width=30)
entry.pack(pady=10)

result_string = tk.StringVar(window, value="")
result = ttk.Label(window, textvariable=result_string, background='lightblue')
result.pack(pady=10)

button = ttk.Button(master=window, text="Convert", command=choose)
button.pack(pady=10)

# Run the window
window.mainloop()
