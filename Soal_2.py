#Soal 2
class Persegi:
  def __init__(self, sisi):
    self.sisi = sisi
  def luas(self):
    return (self.sisi**2)

class Kubus(Persegi):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def luas(self):
    return (self.sisi**3)

objek1 = Persegi(3)
objek2 = Kubus(3)
print("Luas persegi", objek1.luas())
print("Luas kubus", objek2.luas())
