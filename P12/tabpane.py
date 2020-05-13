import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Tabpane:
	def __init__(self, prn):
		self.tab_parent = ttk.Notebook(prn, width = 800, height=500 )
		self.tab = []
		self.canvas = []
		self.im = []
		self.tab_parent.pack(expand=1, side="left")
		self.counter = 0
	
	def addTab(self, imgfile):
		self.tab.append(ttk.Frame(self.tab_parent))
		self.tab_parent.add(self.tab[self.counter], text = "Image "+str(self.counter+1))
		
		self.im.append( ImageTk.PhotoImage(file=imgfile) )
		self.canvas.append(tk.Canvas(self.tab[self.counter], width=800, height=500))
		self.canvas[self.counter].pack()
		canvasImage = self.canvas[self.counter].create_image(0, 0, image=self.im[self.counter], anchor="nw")
		self.counter +=1
	
	def getTab(self):	
		return self.tab_parent
	
	def clearTab(self):
		for i in range(10):
			self.tab[i].destroy()
			self.canvas[i].destroy()
		self.tab_parent.destroy()
		self.tab = []
		self.canvas = []
		self.im = []
		self.counter = 0
		
	def getTab(self):	
		return self.tab_parent

if __name__ == "__main__":

	root = tk.Tk()
	root.geometry("800x500")
	root.title("ImageViewer")

	tab = Tabpane(root)
	img = Image.new('RGB', (500, 500), color = 'white')
	img.save('blank.png')
	for i in range(7):
		tab.addTab("cover"+str(i+1)+".png")

	root.mainloop()