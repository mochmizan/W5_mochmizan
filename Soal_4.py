#Soal 4
import math

class Paket:
  def __init__(self, berat):
    self.berat = berat #dalam kilo
    self.harga = math.ceil(berat / 2) * 18
  
  def __add__(self, other):
    return self.berat + other.berat

Minyak1 = Paket(1.2)
Gula1 = Paket(2)
paket1 = Paket(Minyak1 + Gula1)
print("Berat kedua benda adalah", paket1.berat)
print("Dengan harga pengiriman", paket1.harga)
