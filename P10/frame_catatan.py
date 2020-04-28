import sys
import tkinter

def main():
	#Basic Window
	root = tkinter.Tk()
	
	root.title("MyApp!")
	root.resizable()
	
    #Menu 
	def quit():
		root.destroy()
		
	bar = tkinter.Menu( root )
	fileMenu = tkinter.Menu(bar, tearoff = 0)
	fileMenu.add_command( label = "Exit", command = quit )
	
	bar.add_cascade( label = "File", menu = fileMenu )
	root.config(menu = bar)
	
	#Frame
	mainFrame = tkinter.Frame(root, bg="yellow", padx = 5, pady = 5)
	mainFrame.pack()
	
	#Label
	caption = tkinter.Label(mainFrame, text = "Catatan :")
	caption.pack()
	
	#Text
	note = tkinter.Text(mainFrame, bg="lightgrey", width = 30, height = 15)
	note.pack()
	
	#Button
	def delNote():
		note.delete("1.0",tkinter.END)
		
	tkinter.Button(mainFrame, text="Hapus", command = delNote).pack()

	root.mainloop()
	
if __name__ == "__main__":
	main()

