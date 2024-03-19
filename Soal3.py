
def tampil_deret(tinggi, lebar):
    bil_awal = 1
    for i in range(1, tinggi + 1):
        for j in range(1, lebar + 1):
            print(bil_awal, end=" ")
            bil_awal += 1
        print()

tinggi = int(input("Masukkan tinggi deret: "))
lebar = int(input("Masukkan lebar deret: "))
tampil_deret(tinggi, lebar)