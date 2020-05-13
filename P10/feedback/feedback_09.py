from tkinter import *
def main():
		def save():								#apakah program sudah dirunning sebelum di submit?
				#firstname = firstname.get()	#name conflict, firstname (local variable) dgn firstname = StringVar()
				fn= firstname.get()				#sama halnya dengan lastname, dan zipcode
				ln = lastname.get()
				#adr = address.get()			#address undefined! karena yg didefinisikan adress [baris 40] bukan address
				adr = adress.get()				
				zc = zipcode.get()
				#ph = phone.get()				#phone atau nophone??  nophone = IntVar()
				ph = nophone.get()				
				#file.open("user_Data.txt","w")	#file = open("user_Data.txt","w")
				file = open("user_Data.txt","w")
				file.write(fn)
				file.write(ln)
				file.write(adr)
				#file.write(zc)					#konversi ke string, zc = zipcode.get() [baris 9], zipcode = IntVar() [baris 53] --> tipe data integer
				file.write(str(zc))
				#file.write(ph)					#konversi ke string, ph = nophone.get() [baris 11], nophone = IntVar() [baris 54] --> tipe data integer
				file.write(str(ph))
				file.close()
		def quit():
				root.destroy

		root = Tk()
		root.geometry("500x400")
		root.title("Form")

		menu_bar= Menu()
		root.config(menu=menu_bar)

		sub_menu = Menu(menu_bar)
		menu_bar.add_cascade(label= "File", menu=sub_menu)
		sub_menu.add_command(label = "Save", command=save)
		sub_menu.add_separator()
		sub_menu.add_command(label="Exit",command=quit)

		firstname_form = Label(text="First name",)
		lastname_form = Label(text = "Last name",)
		adress_form = Label(text = "Adress",)
		zipcode_form = Label(text = "Zipcode",)
		nophone_form = Label(text= "Phone Number")

		firstname_form.place(x = 15, y = 50)
		lastname_form.place(x = 15, y = 80)
		adress_form.place(x = 15, y = 110)
		zipcode_form.place(x = 15, y = 140)
		nophone_form.place(x = 15, y = 170)

		firstname = StringVar()
		lastname = StringVar()
		adress = StringVar()
		zipcode = IntVar()
		nophone = IntVar()

		firstname_entry = Entry(textvariable = firstname, width = "30")
		lastname_entry= Entry(textvariable = lastname, width = "30")
		adress_entry = Entry(textvariable = adress, width = "30")
		zipcode_entry = Entry(textvariable = zipcode, width = "30")
		nophone_entry = Entry(textvariable = nophone, width = "30")

		firstname_entry.place(x = 150, y = 50)
		lastname_entry.place(x = 150, y = 80)
		adress_entry.place(x = 150, y = 110)
		zipcode_entry.place(x = 150, y = 140)
		nophone_entry.place(x = 150, y = 170)

		savebutton = Button(root, text = "Save", width = "30", height = "2", command=save)
		savebutton.place(x = 15, y = 210)

		root.mainloop()

if __name__ == "__main__":
	main()
		   
