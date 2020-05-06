
from class_pegawai import Pegawai
from class_transaksi import Transaksi

if __name__ == "__main__":
	Marketer = Pegawai("Andi", 20)
	Bendahara = Pegawai("Budi", 22)
	
	Marketer.golongan = 2
	Marketer.ambil_cuti(3)
	
	bayar_gaji = Transaksi(Bendahara, Marketer)
	bayar_gaji.kirim()
	print(bayar_gaji.laporan())

	