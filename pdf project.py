# Create a Python project to encrypt the pdf file
import tkinter as tk
from PyPDF2 import PdfWriter, PdfReader
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox

filename = ""
passwd = ""
psd_entry = ""

def select_pdf():
    global filename
    global psd_entry
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    if filename:  # Ensure a file was selected
        file_label.config(text=f"Selected file: {filename}")
        psd_label.grid(row=3, column=0, pady=10)
        psd_entry.grid(row=3, column=1, columnspan=2, pady=10)
        lock_button.grid(row=4, column=0, columnspan=8, pady=10)

def encrypt():
    global filename
    global passwd
    
    if not filename:
        messagebox.showerror("Error", "Please select a PDF file first.")
        return

    passwd = psd_entry.get()
    
    if not passwd:
        messagebox.showerror("Error", "Please enter a password.")
        return
    
    out = PdfWriter()
    file = PdfReader(filename)
    
    # Use len(reader.pages) instead of reader.numPages
    num = len(file.pages)

    for idx in range(num):
        page = file.pages[idx]  # Access pages using the index
        out.add_page(page)
    
    try:
        # Save the encrypted PDF with a modified name
        output_filename = f"encrypted_{filename.split('/')[-1]}"
        with open(output_filename, "wb") as f:
            out.encrypt(passwd)
            out.write(f)
        messagebox.showinfo("Success", f"File saved as {output_filename}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the Tkinter window
window = tk.Tk()
window.geometry('400x250')
window.title("PDF LOCKER")

# Add the title label
title = tk.Label(window, text='PDF LOCKER', font=('arial', 25), justify="center")
title.grid(row=0, column=0, columnspan=8)

# Add the file selection label and button
label1 = ttk.Label(window, text='Select file:')
label1.grid(row=1, column=0, pady=10)

select_file = ttk.Button(window, text="Choose file", command=select_pdf)
select_file.grid(row=1, column=1, pady=10)

# Label to show selected file
file_label = tk.Label(window, text="No file selected", bg="lightgray", width=35)
file_label.grid(row=2, column=0, columnspan=2, padx=5)

# Password entry field
psd_label = tk.Label(window, text="Password for PDF:")
psd_entry = tk.Entry(window, width=25)

# Encrypt button
lock_button = ttk.Button(window, text="Encrypt file", command=encrypt, width=30)

# Start the Tkinter main loop
window.mainloop()
 
