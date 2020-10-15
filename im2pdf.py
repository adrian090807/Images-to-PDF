import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
files = filedialog.askopenfilename(multiple=True) 
var = root.tk.splitlist(files)

images=[]
for i in files:
    images.append(Image.open(i))

im1=images.pop(0)
dir = filedialog.askdirectory()

filename = "Images.pdf"
filepath = os.path.join(dir,filename)

im1.save(filepath, "PDF" ,resolution=100.0, save_all=True, append_images=images)
