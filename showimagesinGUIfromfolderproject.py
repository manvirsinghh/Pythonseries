from tkinter import Tk
from PIL import Image,ImageTk
import tkinter as tk

import os
root=tk.Tk()
root.geometry("500x300")
root.title("image viewer")
img_folder_path=r"c:\Users\Win\Pictures\Camera Roll"
image_files = [f for f in os.listdir(img_folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
images=[]
for file in image_files:
    image_path=os.path.join(img_folder_path,file)
    image=Image.open(image_path)
    images.append(ImageTk.PhotoImage(image))
current_image_index=0

image_label = tk.Label(root, image=images[current_image_index])
image_label.pack()


def update_img():
    image_label.config(image=images[current_image_index])
   

def next_img():
    global current_image_index
    if current_image_index<len(images)-1:
        current_image_index+=1
        update_img()

def prev_img():
     global current_image_index
     if current_image_index>0:
        current_image_index-=1
        update_img()

button_next=tk.Button(root,text="next",command=next_img)
button_next.pack(side="right",padx=10)
button_prev=tk.Button(root,text="prev",command=prev_img)
button_prev.pack(side="left",padx=10)


label=tk.Label(root,text="IMAGE VIEWER")
label.pack()





root.mainloop()

