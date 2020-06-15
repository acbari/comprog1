#import modulluas
from modulluas import luasKotak, mobil, salam
from modulluas import luasLingkaran as luas

sisiKotak = 10
#print(modulluas.luasKotak(10))
print(luas(5))

avanza = mobil("Avanza", 200)
#print(type(avanza))
print(str(avanza))
print(str(avanza)[-3:])
#print(salam)

print("Harga setelah diskon 20% :", 0.8*int(avanza))

