class Pegawai:
	def __init__(self, nama, umur):
		self.nama = nama
		self.umur = umur
		self.golongan = 1
		self.jumlah_cuti = 0
	def __str__(self):
		return self.nama + ' berumur ' + str(self.umur)

if __name__ == "__main__":
	Marketer = Pegawai("Andi", 20)
	Bendahara = Pegawai("Budi", 22)

	print(Marketer)
	print(Bendahara)
