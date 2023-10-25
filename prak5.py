# No1
kendaraan=['motor','vario',125,'merah',2]
print(kendaraan)

kendaraan=['motor','vario',125,'merah',2]
kendaraan.append('25.200.000')
kendaraan.append('matic')
print(kendaraan)

kendaraan=['motor','vario',125,'merah',2]
kendaraan.append('25.200.000')
kendaraan.append('matic')
kendaraan.insert(2,'honda')
print(kendaraan)

#  No2
#Tugas2
operasi = input("Menghitung luas bangun datar")
match operasi:
  case "1":
    sisi= int (input("masukan nilai sisi:"))
    luas= sisi*sisi
    print(luas)
  case "2":
    jari_jari= float (input("masukan nilai jari jari:"))
    luas= 3.14*jari_jari*jari_jari
    print(luas)
  case "3":
    alas= float (input("masukan nilai alas:"))
    tinggi= float(input("masukan nilai tinggi:"))
    luas= 0.5*alas*tinggi
    print(luas)  
  case _:
    print("salah pilih")

# cara pak reza 
print ("""Selamat datang di aplikasi menghitung luas bangun datar. silahkan pilih salah satu menu dibawah ini: 
      1. Menghitung Luas Persegi
       2. Menghitung Luas Lingkaran 
       3.Menghitung Luas Segitiga 
       """)

pilihan = int(input('masukan pilihan kamu'))

match pilihan:
    case 1 : 
        print('kamu memilih 1 untuk menghitung luas persegi')
        sisi = int(input('masukan sisi'))
        luasP= sisi*sisi 
        print('luas persegi dengan', sisi, 'adalah', luasP)
    case 2 : 
        print('kamu memilih 2 untuk menghitung luas lingkaran')
        r = float(input('masukan jari-jari lingkaran'))
        luasL = 3,14 * r * r
        int ('luas lingkaran dengan', r, 'adalah ', int(luasL))

    case 3 : 
      print('kamu memilih 3 untuk menghitung luas segitiga')
      alas =  int(input('masukan alas'))
      tinggi = int(input('masukan tinggi'))
      lSegitiga= 0,5 * alas * tinggi 
      print ('luas segitiga yang adalah', int(lSegitiga))

    case _:
      print('kamu salah masukan pilihan')




  
  