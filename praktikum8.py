#No 1
def profil(nama,alamat,gender,umur,hoby):

    print("nama saya adalah",nama)
    print("alamat saya di",alamat)
    print("gender saya adalah",gender)
    print("umur saya",umur)
    print("hoby saya adalah",hoby)

profil("fani", "depok", "Perempuan", "17 Tahun", "Mendengarkan musik")

print("=========================================")

#No2
def cetak_nilai(nilai):
    if(nilai <=60):
        print("gagal")
    elif(nilai >=61 and nilai <=70):
        print("baik")
    elif(nilai >=71 and nilai <=80):
        print("sangat baik")
    elif(nilai >= 81 and nilai <=100):
        print("istemewa")
    else:
        print("nilai tidak ada")

cetak_nilai(60)
cetak_nilai(74)
cetak_nilai(98)

print("========================================")

#No 3
def bilangan_ganjil(ganjil):

    for i in range(ganjil):
        if (i %2 !=0):
            print(i,end='  ')
bilangan_ganjil(100)