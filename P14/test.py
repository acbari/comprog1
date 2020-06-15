class Buah:
	def __init__(self, nama, berat, harga):
		self.nama = nama
		self.berat = berat
		self.hargaperkilo =  harga
	
	def hitungHarga(self):
		return "Rp "+str(self.berat * self.hargaperkilo)

	def hitungBerat(self):
		return str(self.berat) +" Kg"

class BBM:
	def __init__(self, nama, kapasitas, harga, berat):
		self.nama = nama
		self.kapasitasbbm = kapasitas
		self.hargaperliter =  harga
		self.berat = berat
		
	def hitungHarga(self):
		return "Rp "+str(self.kapasitasbbm * self.hargaperliter)

	def hitungBerat(self):
		return str(self.berat) +" Kg"

def cetakharga(item):
	print("Harga "+item.nama+": "+item.hitungHarga())
	
def cetakBerat(item):
	print("Berat "+item.nama+": "+item.hitungBerat())
	
	
jeruk = Buah("Jeruk", 2, 20000)
bensin = BBM("Bensin Avanza", 45, 10000, 1600)

daftarBelanja = [jeruk, bensin]
for item in daftarBelanja:
	cetakharga(item)
	cetakBerat(item)

#cetakharga(jeruk)
#cetakharga(bensin)
