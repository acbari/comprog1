import tkinter as tk
import json

class DragDropMixin:
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.make_draggable(self)
		
	def make_draggable(self, widget):
		widget.bind("<Button-1>", self.on_drag_start)
		widget.bind("<B1-Motion>", self.on_drag_motion)
		
	def on_drag_start(self, event):
		widget = event.widget
		widget._drag_start_x = event.x
		widget._drag_start_y = event.y

	def on_drag_motion(self, event):
		widget = event.widget
		x = widget.winfo_x() - widget._drag_start_x + event.x
		y = widget.winfo_y() - widget._drag_start_y + event.y
		if x< 0:
			x = 0
		if y< 0:
			y=0
		grid = 5
		self.dx = x//grid*grid
		self.dy = y//grid*grid
		widget.place(x=self.dx, y=self.dy)

class DnDFrame(DragDropMixin, tk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
root = tk.Tk()
root.title("latihan")
root.geometry("500x500")
frame = DnDFrame(root, width= 300, height=300, bg="red")
frame.place(x=0,y=0)

tk.Label(frame, text="Hello world").place(x=0,y=0)

root.mainloop()