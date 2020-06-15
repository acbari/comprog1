#import Tkinter
import tkinter as tk
import json

root = tk.Tk()
root.title("latihan")
root.geometry("300x300")

#frame = tk.Frame(root,width= 300, height=300)
frame = DnDFrame(root,width= 300, height=300)
frame.grid(row=0)
label1 = tk.Label(frame, text="Formulir")
label1.grid(row=0, column=0)
tk.Label(frame, text="Name").grid(row=1, column=0)
nama = tk.Entry(frame)
nama.grid(row=1, column=1)
tk.Label(frame, text="Umur").grid(row=2, column=0)
umur = tk.Entry(frame)
umur.grid(row=2, column=1)

def saveData(event):
	data = {}
	data["nama"] = nama.get()
	data["umur"] = umur.get()
	outfile = open("data.json","w")
	hasil = json.dumps( data )
	outfile.write(hasil )
	outfile.close()
	#json.dump( data , outfile )

	

tk.Button(frame,text="Save",command=saveData).grid(row=3)
label1.bind("<Button-1>", saveData)

root.mainloop()