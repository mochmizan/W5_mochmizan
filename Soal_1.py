#Soal 1
class Segitiga:
  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi
  def luas(self):
    return (self.alas*self.tinggi/2)

class Persegi:
  def __init__(self, sisi):
    self.sisi = sisi
  def luas(self):
    return (self.sisi**2)

objek1 = Segitiga(3, 4)
objek2 = Persegi(4)
print("Luas segitiga", objek1.luas())
print("Luas persegi", objek2.luas())
