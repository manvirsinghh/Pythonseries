import tkinter as tk
from tkinter import filedialog, font, messagebox
import os

# Create the root window
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

# Create text area
text_area = tk.Text(root, wrap="word", font=("Arial", 12), undo=True)
text_area.pack(expand=True, fill="both")

# Add a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: new_file())
file_menu.add_command(label="Open", command=lambda: open_file())
file_menu.add_command(label="Save", command=lambda: save_file())
file_menu.add_command(label="Save As", command=lambda: save_as())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: exit_app())

# Create the Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Bold", command=lambda: bold_text())
edit_menu.add_command(label="Italic", command=lambda: italic_text())
edit_menu.add_command(label="Underline", command=lambda: underline_text())
edit_menu.add_command(label="Clear Formatting", command=lambda: clear_formatting())
edit_menu.add_separator()
edit_menu.add_command(label="Word Count", command=lambda: update_word_count())

# Create the View menu for Dark Mode and other features
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Toggle Dark Mode", command=lambda: toggle_dark_mode())
view_menu.add_command(label="Align Left", command=lambda: align_left())
view_menu.add_command(label="Align Center", command=lambda: align_center())
view_menu.add_command(label="Align Right", command=lambda: align_right())
view_menu.add_separator()
view_menu.add_command(label="Increase Font Size", command=lambda: change_font_size(2))
view_menu.add_command(label="Decrease Font Size", command=lambda: change_font_size(-2))

# Add a status bar for word count
status_bar = tk.Label(root, text="Words: 0, Characters: 0", bd=1, relief="sunken", anchor="w")
status_bar.pack(side="bottom", fill="x")

# Set up dark mode flag
is_dark_mode = False
current_font_size = 12

# Step 1: Define methods for file management
def new_file():
    text_area.delete("1.0", "end")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete("1.0", "end")
            text_area.insert("1.0", file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", "end-1c"))

def save_as():
    save_file()

# Step 2: Define methods for text formatting
def bold_text():
    current_font = text_area.cget("font")
    new_font = (current_font[0], current_font[1], 'bold')
    text_area.config(font=new_font)

def italic_text():
    current_font = text_area.cget("font")
    new_font = (current_font[0], current_font[1], 'italic')
    text_area.config(font=new_font)

def underline_text():
    current_font = text_area.cget("font")
    new_font = (current_font[0], current_font[1], 'underline')
    text_area.config(font=new_font)

def clear_formatting():
    text_area.config(font=("Arial", current_font_size))

# Step 3: Define methods for word count and character count
def update_word_count(event=None):
    text = text_area.get("1.0", "end-1c")  # Get all text
    word_count = len(text.split())
    char_count = len(text.replace(" ", ""))
    status_bar.config(text=f"Words: {word_count}, Characters: {char_count}")

# Step 4: Define method for Dark Mode toggle
def toggle_dark_mode():
    global is_dark_mode
    if is_dark_mode:
        text_area.config(bg="white", fg="black")
        status_bar.config(bg="lightgrey", fg="black")
        root.config(bg="lightgrey")
        is_dark_mode = False
    else:
        text_area.config(bg="black", fg="white")
        status_bar.config(bg="black", fg="white")
        root.config(bg="black")
        is_dark_mode = True

# Step 5: Methods for alignment
def align_left():
    text_area.tag_configure("left", justify="left")
    text_area.tag_add("left", "1.0", "end")

def align_center():
    text_area.tag_configure("center", justify="center")
    text_area.tag_add("center", "1.0", "end")

def align_right():
    text_area.tag_configure("right", justify="right")
    text_area.tag_add("right", "1.0", "end")

# Step 6: Method to change font size
def change_font_size(increment):
    global current_font_size
    current_font_size += increment
    text_area.config(font=("Arial", current_font_size))

# Step 7: Exit confirmation
def exit_app():
    if messagebox.askyesno("Exit", "Do you want to save changes before exiting?"):
        save_file()
    root.quit()

# Run the Tkinter event loop
root.mainloop()
