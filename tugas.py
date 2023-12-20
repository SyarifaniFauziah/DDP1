class Animal:
    def __init__(self, nama, makanan, hidup, berkembangbiak):
          self.nama = nama
          self.makanan = makanan
          self.hidup = hidup
          self.berkembangbiak = berkembangbiak

    def cetak(self):
         print("Saya adalah", self.nama, "Makanan saya ", self.makanan, "Saya hidup di", self.hidup, "Saya berkembang biak secara", self.berkembangbiak)

class Badak(Animal):
     def __init__(self, nama, makanan, hidup, berkembangbiak, bergerak, bernafas):
          super().__init__(nama, makanan, hidup, berkembangbiak)
          self.bergerak = bergerak
          self.bernafas = bernafas
        
     def cetak(self):
          super().cetak()
          print("Hewan ini bergerak dengan cara", self.bergerak)
          print("Hewan ini bernafas dengan", self.bernafas)

class ikan(Animal):
      def __init__(self, nama, makanan, hidup, berkembangbiak, bergerak, bernafas):
          super().__init__(nama, makanan, hidup, berkembangbiak)
          self.bergerak = bergerak
          self.bernafas = bernafas
        
      def hasil(self):
          super().cetak()
          print("Hewan ini bergerak dengan cara", self.bergerak)
          print("Hewan ini bernafas dengan", self.bernafas)

class ular(Animal):
      def __init__(self, nama, makanan, hidup, berkembangbiak, bergerak, bernafas):
          super().__init__(nama, makanan, hidup, berkembangbiak)
          self.bergerak = bergerak
          self.bernafas = bernafas
        
      def tampil(self):
          super().cetak()
          print("Hewan ini bergerak dengan cara", self.bergerak)
          print("Hewan ini bernafas dengan", self.bernafas)

#objek Badak
y = Badak("Badak", "Tumbuhan", "daratan", "melahirkan", "berjalan", "Paru-Paru")
y.cetak()

#objek Ikan 
z = ikan("Ikan Cupang", "Pelet", "Air", "bertelur", "berenang", "Insang")
z.hasil()

#objek ular 
a = ular("ular", "Daging", "Daratan", "bertelur", "Melata", "Kulit")
a.tampil()


          