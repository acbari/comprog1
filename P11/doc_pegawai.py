class Pegawai:
	""" class  merepresentasikan pegawai di dunia nyata
		memiliki atribut nama, umur, golongan, dan jumlah cuti
		memiliki method perhitungan gaji dan penambahan jumlah cuti
	"""
	def __init__(self, nama, umur):
		self.nama = nama
		self.umur = umur
		self.golongan = 1
		self.jumlah_cuti = 0
	
	def hitung_gaji(self):
		""" Fungsi untuk menghitung gaji pegawai berdasarkan UMR, tingkat   
		golongan dan jumlah cuti """
		
		UMR = 3623778.91
		return UMR + self.golongan * 500000 - self.jumlah_cuti * 100000
	
	def __str__(self):
		return self.nama + ' berumur ' + str(self.umur)

if __name__ == "__main__":
	Marketer = Pegawai("Andi", 20)
	print(Marketer.__doc__)
	print(Marketer.hitung_gaji.__doc__)
