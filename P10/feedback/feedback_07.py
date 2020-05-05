import sys, random
from tkinter import *
from tkinter.filedialog import asksaveasfile

#savedata harus mengambil data dari widget entry dan menyimpan data ke file
#letakkan fungsi setelah deklarasi widget entry
''' 									#original location of savedata
def savedata():
   data = note.get("1.0", root.END)
   f = open("data.txt", 'w')
   f.write(data)
   f.close()
'''

root = Tk()
root.geometry("230x140")

#karena file menu berisi menu yang memanggil savedata,
#maka file menu harus diletakkan seetelah deklarasi setelah deklarasi fungsi savedata
'''										#original location of menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=savedata)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
'''

Label(root, text='First Name').grid(row=0) 
Label(root, text='Last Name').grid(row=1) 
Label(root, text='Address').grid(row=2)
Label(root, text='Zip Code').grid(row=3)
Label(root, text='Phone Number').grid(row=4)

e1 = Entry(root) 
e2 = Entry(root)
e3 = Entry(root) 
e4 = Entry(root) 
e5 = Entry(root) 

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
e3.grid(row=2, column=1) 
e4.grid(row=3, column=1) 
e5.grid(row=4, column=1) 

#deklarasi fungsi savedata setelah deklarasi widget entry, karena harus mengambil data dari widget tersebut
def savedata():
	#data = note.get("1.0", root.END) 			# tidak ada widget/ui yang bernama note!
	#gunakan dictionary untuk menyimpan data, ambil data dari widget entry
	data = {}
	data['First Name'] =  e1.get()
	data['Last Name'] = e2.get()
	data['Address'] = e3.get()
	data['Zip Code'] = e4.get()
	data['Phone Number'] = e5.get()
	f = open("data.txt", 'w')
	f.write(str(data))					#untuk simpan ke format json: import json
										#f.write(json.dumps(data))
	f.close()
	print("simpan ke","data.txt")

#deklarasi menu setelah deklarasi fungsi savedata, karena salah satu item menu ada yang memanggil fungsi tersebut
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=savedata)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

saveButton = Button(root, text="Save", command = savedata)
saveButton.grid(row=5, column=1)

root.mainloop()