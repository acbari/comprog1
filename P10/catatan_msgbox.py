import sys
import tkinter, tkinter.messagebox

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
	
	#Label
	caption = tkinter.Label(root, text = "Catatan :")
	caption.pack()
	
	#Text
	note = tkinter.Text(root, bg="lightgrey", width = 30, height = 15)
	note.pack()
	
	#Button
	def msgBox1():
		tkinter.messagebox.showinfo("Info Box", "Kamu dapat menghapus catatan dengan menekan Tombol-3.")
	def msgBox2():
		tkinter.messagebox.showwarning("Warning Box", "Sebelum dihapus pastikan catatan tidak sedang dipakai!")
	def msgBox3():
		answer = tkinter.messagebox.askyesno("Yes/No Box", "Apakah kamu ingin menghapus catatan?")
		if answer:
			note.delete("1.0",tkinter.END)
		else:
			pass
	tkinter.Button(root, text="Tombol-1", command = msgBox1).pack(side=tkinter.LEFT)
	tkinter.Button(root, text="Tombol-2", command = msgBox2).pack(side=tkinter.LEFT)
	tkinter.Button(root, text="Tombol-3", command = msgBox3).pack(side=tkinter.LEFT)

	root.mainloop()
	
if __name__ == "__main__":
	main()
