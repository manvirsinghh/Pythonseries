import tkinter as tk
from time import strftime
root=tk.Tk()
root.geometry("300x200")
root.title("Digital Clock")
def time():
 current_time=strftime("%H:%M:%S %p")
 label.config(text=current_time)
 label.after(1000,time)



label=tk.Label(root,text="DIGITAL CLOCK",anchor="center",font=("arial",20,'bold'),background="white",foreground="black")
label.pack() 
time()
root.mainloop()