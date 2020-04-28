import sys, random
import tkinter

def main():
	#Basic Window
	root = tkinter.Tk()
	root.title("Random number generator")
	root.resizable(width = True ,height = False )

    #Menu 
	def quit():
		root.destroy()
	bar = tkinter.Menu( root )
	fileMenu = tkinter.Menu(bar, tearoff = 0)
	fileMenu.add_command( label = "Exit", command = quit )
	bar.add_cascade( label = "File", menu = fileMenu )
	root.config(menu = bar)
		
	#Frame
	mainFrame = tkinter.Frame(root, borderwidth = 1, padx = 5, pady = 5)
	mainFrame.pack()
	#Text
	note = tkinter.Text(mainFrame, bg="white", width = 30, height = 15)
	note.pack()
	#Button
	def genRnd():
		note.insert( tkinter.END , str(random.randint(0,100))+"\n" )
	def clearTxt():
		note.delete("1.0",tkinter.END)
	def saveTxt():
		data = note.get("1.0",tkinter.END)
		f = open("rand.txt",'w')
		f.write(data)
		f.close()
	tkinter.Button(mainFrame, text="Random", command = genRnd).pack(side=tkinter.LEFT)
	tkinter.Button(mainFrame, text="Clear", command = clearTxt).pack(side=tkinter.LEFT)
	tkinter.Button(mainFrame, text="Save", command = saveTxt).pack(side=tkinter.LEFT)

	root.mainloop()
	
if __name__ == "__main__":
	main()
