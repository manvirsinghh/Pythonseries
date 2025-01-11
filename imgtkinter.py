# from PIL import Image

# # Open the image you want to convert
# img = Image.open(r"c:\Users\Win\Documents\download.jfif")  # Replace with the path to your image

# # Save the image in a different format (e.g., PNG)
# img.save(r"converted_image.png", "PNG")  # Replace with the desired output format

#pillow (python image library) module is used to convert image format to other format) using 
#how to add image to gui
from tkinter import Tk
import tkinter as tk
from tkinter import *
root=tk.Tk()
root.geometry("200x100")
root.title("how to add image in gui")
photo=PhotoImage(file=r"converted_image.png")
label=tk.Label(image=photo)
label.pack()
root.mainloop()
