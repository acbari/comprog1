class Pegawai:
	def __init__(self, nama, umur):
		self.nama = nama
		self.umur = umur
		self.golongan = 1
		self.jumlah_cuti = 0
	
	def __str__(self):
		return self.nama + ' berumur ' + str(self.umur)
	
	def hitung_gaji(self):
		UMR = 3623778.91
		return UMR + self.golongan * 500000 - self.jumlah_cuti * 100000
	
if __name__ == "__main__":
	Marketer = Pegawai("Andi", 20)
	Marketer.golongan = 2

	print("Gaji marketer: Rp ",Marketer.hitung_gaji())
