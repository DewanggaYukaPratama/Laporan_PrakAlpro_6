

def prima(bil):
    if bil < 2:
        return False
    for i in range(2, int(bil ** 0.5) + 1):
        if bil % i == 0:
            return False
    return True

def cari_prima(n):
    prima_terdekat = None
    for i in range(n - 1, 1, -1):
        if prima(i):
            prima_terdekat = i
            break
    return prima_terdekat

n = int(input("Masukkan bilangan (n): "))
prima_terdekat = cari_prima(n)

if prima_terdekat:
    print(f"Bilangan prima terdekat yang kurang dari {n} adalah {prima_terdekat}.")
else:
    print(f"Tidak ditemukan bilangan prima yang kurang dari {n}.")