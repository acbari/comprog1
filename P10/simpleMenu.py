
import tkinter

def main():
	root = tkinter.Tk()
	
	root.title("MyApp!")
	root.geometry("200x200")
	
	def quit():
		root.destroy()
		
	bar = tkinter.Menu( root )
	fileMenu = tkinter.Menu(bar, tearoff = 0)
	fileMenu.add_command( label = "Exit", command = quit )
	
	bar.add_cascade( label = "File", menu = fileMenu )
	root.config(menu = bar)
	
	root.mainloop()
	
if __name__ == "__main__":
	main()

