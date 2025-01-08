# #how to use tkinter library to create desktop applications with graphical user interface
# # Create First Tkinter GUI Application
# # To create a Tkinter Python app, follow these basic steps:

# # Import the tkinter module: Import the tkinter module, which is necessary for creating the GUI components.
# # Create the main window (container): Initialize the main application window using the Tk() class.
# # Set Window Properties: We can set properties like the title and size of the window.
# # Add widgets to the main window: We can add any number of widgets like buttons, labels, entry fields, etc., to the main window to design the interface.
# # Pack Widgets: Use geometry managers like pack(), grid() or place() to arrange the widgets within the window.
# # Apply event triggers to the widgets: We can attach event triggers to the widgets to define how they respond to user interactions.
# import tkinter as tk
# #create a main window
# root=tk.Tk()
# root.geometry("400x250")#set window size
# root.title("Welcome to my app")#set window title

# #create a label widget with all options
# label=tk.Label(root,text="",anchor="center",background="lightblue",height=100,width=100,justify="center")
# #pack the label into window
# label.pack(pady=20)#add padding to the top
# entry=tk.Entry(root, width=30)
# entry.pack(pady=10)
# def show_text():
#  text=entry.get()
# text_var.set(f"You entered: {text}")
# button=tk.Button(root,width=30,text="submit",command=show_text)
# button.pack(pady=10)
#  #run the main event loop
# root.mainloop()

import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x250")  # Set window size
root.title("Welcome to my app")  # Set window title

# Create a StringVar() to hold the text dynamically
text_var = tk.StringVar()
# StringVar() is a special type of variable used in Tkinter to store and manage text values (strings).
text_var.set("Enter something below:")
# The .set() method is used to set the value of the StringVar(). It is like assigning a value to a normal Python variable but in a way that any widgets bound to it will automatically update when the value changes.
# Create a label widget with textvariable
label = tk.Label(
    root,
    textvariable=text_var,
    anchor="center",
    background="lightblue",
    height=2,
    width=40,
    justify="center"
)
# Pack the label into window
label.pack(pady=20)  # Add padding to the top

# Create an entry widget to take user input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Function to update label when button is clicked
def show_text():
    text = entry.get()  # Get text from entry widget
    text_var.set(f"You entered: {text}")  # Update the text_var, which updates the label text

# Create a button widget
button = tk.Button(root, width=30, text="Submit", command=show_text)
button.pack(pady=10)

# Run the main event loop
root.mainloop()
