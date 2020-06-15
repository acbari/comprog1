import math

salam = "Hello world"

def luasKotak(sisi):
    return sisi*sisi
    
def luasLingkaran(radius):
	return math.pi * radius * radius
    
class mobil:
	def __init__(self, nama, harga):
		self.nama = nama
		self.harga  = harga
		
	def __str__(self):
		return self.nama +" berharga "+ str(self.harga) +" Juta"
		
	def __int__(self):
		return self.harga

	def hitungHarga(self):
		return self.harga * 1000000


class Buah:
	def __init__(self, nama, berat, hargaperkilo):
		self.nama = nama
		self.hargaperkilo = hargaperkilo
		self.berat = berat
		
	def __str__(self):
		return self.nama +" berharga "+ str(self.harga)
		
	def __int__(self):
		return self.harga
		
	def hitungHarga(self):
		return self.hargaperkilo * self.berat
		
def HitungHarga(barang):
	hasil  = barang.hitungHarga()
	print("harga "+barang.nama+": Rp "+ str( hasil ) )
	return hasil
	
truk = mobil("Truck",500)
mangga = Buah("Mangga",2,15000)
#HitungHarga(truk)
#HitungHarga(mangga)

daftarbarang = [truk, mangga]
total = 0
for item in daftarbarang:
	total += HitungHarga(item)
print("Total harga:", total)
