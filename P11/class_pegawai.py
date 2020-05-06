class Pegawai:
	def __init__(self, nama, umur):
		self.nama = nama
		self.umur = umur
		self.golongan = 1
		self.jumlah_cuti = 0
	
	def hitung_gaji(self):
		UMR = 3623778.91
		return UMR + self.golongan * 500000 - self.jumlah_cuti * 100000
		
	def ambil_cuti(self, jumlah_hari):
		self.jumlah_cuti = self.jumlah_cuti + jumlah_hari

	
if __name__ == "__main__":
	Marketer = Pegawai("Andi", 20)
	Marketer.golongan = 2
	Marketer.ambil_cuti(3)
	print("Jumlah cuti: ",Marketer.jumlah_cuti)
	print("Gaji marketer: Rp ",Marketer.hitung_gaji())


