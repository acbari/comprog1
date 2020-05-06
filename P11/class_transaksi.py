from datetime import datetime as dt

class Transaksi:
	def __init__(self, pengirim, penerima):
		self.pengirim = pengirim
		self.penerima = penerima
		self.waktu_kirim = None
		self.jumlah = 0
	
	def kirim(self):
		self.jumlah = self.penerima.hitung_gaji()
		self.waktu_kirim = dt.now()
	
	def laporan(self):
		data_laporan = 'Gaji telah dibayar oleh ' + self.pengirim.nama +'\n'
		data_laporan += ' ke ' + self.penerima.nama +'\n'
		data_laporan += ' sebesar: Rp ' + str(self.jumlah) +'\n'
		data_laporan += ' pada: ' + str(self.waktu_kirim) 
		return data_laporan

if __name__ == "__main__":
	Marketer = Pegawai("Andi", 20)
	Bendahara = Pegawai("Budi", 22)
	
	Marketer.golongan = 2
	Marketer.ambil_cuti(3)
	
	gaji_Mei = Transaksi(Bendahara, Marketer)
	gaji_Mei.kirim()
	print(gaji_Mei.laporan())
