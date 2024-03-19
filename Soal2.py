

def faktor(bil):
    if bil == 0:
        return 1
    else:
        return bil * faktor(bil - 1)

n = int(input("Masukkan nilai n: "))

for i in range(n, 0, -1):
    print(faktor(n), end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    