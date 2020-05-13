import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x500")
root.title("ImageViewer")

frame = tk.Frame(root)
imgfile = 'cover1.png'
im = ImageTk.PhotoImage(file=imgfile)
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()
canvasImage = canvas.create_image(0, 0, image=im, anchor="nw")

root.mainloop()