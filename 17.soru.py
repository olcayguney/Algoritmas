# X ve Y pozitif birer sayı olmak üzere , eğer X sayısının çarpanları toplamı Y sayısana ayrıca Y sayısının çarpanları toplamı X sayısına
# eşit ise bu sayıları dost sayılar denir. Dost sayı olup olmadığını bulan bir program yazınız.

def DostSayi(x, y):
    xCarpanList = []
    yCarpanList = []

    for i in range(1, x // 2 + 1):
        if x % i == 0:
            xCarpanList.append(i)
    for i in range(1, y // 2 + 1):
        if y % i == 0:
            yCarpanList.append(i)

    return x == sum(yCarpanList) and y == sum(xCarpanList)


xNum = int(input("İlk sayıyı giriniz: "))
yNum = int(input("İkinci sayıyı giriniz: "))

if DostSayi(xNum, yNum):
    print(f"{xNum} ve {yNum} dost sayılardır.")
else:
    print(f"{xNum} ve {yNum} dost sayı değildir.")
