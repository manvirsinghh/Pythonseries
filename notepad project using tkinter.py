from tkinter import Tk
import tkinter as tk
from tkinter import messagebox,filedialog
root=tk.Tk()
root.title("NOTEPAD")
root.geometry("300x500")
def new_file():
   text_area.delete(0,tk.END)
def open_file():
   file=filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
   if file:
        with open(file, "r") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())
def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))

def cut_text():
    text_area.event_generate("<<cut>>")
def copy_text():
    text_area.event_generate("<<copy>>")
def paste_text():
    text_area.event_generate("<<paste>>")
def about():
    messagebox.showinfo("about","Notepad made using tkinter")

label=tk.Label(root,text="NOTEPAD",justify="left",background="white",foreground="black")
label.pack()

text_area=tk.Text(root,wrap="word",font=('arial,20'))
text_area.pack()
menu_bar=tk.Menu(root)

file_menu=tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="new",command=new_file)
file_menu.add_command(label="edit",command=open_file)
file_menu.add_command(label="save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="exit",command=root.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)
root.mainloop()
