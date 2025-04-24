# Girilen sayının Smith sayı olup olmadığını bulan program.
# Smith sayısı: Sayı 1'den büyük ve asal olmamalıdır. Sayının rakamlarının toplamı, asal çarpanlarının rakamlarının toplamına eşit olmalıdır.

def smith_mi(sayi):
    asal_bolenler = bolen_bul(sayi)
    if len(asal_bolenler) == 0 or sayi == 1:
        print("Sayınız asal sayıdır - Smith değildir!")
        return False
    else:
        bolen_toplami = sum(sum(int(rakam) for rakam in str(b)) for b in asal_bolenler)
        sayi_toplami = sum(int(rakam) for rakam in str(sayi))
        return sayi_toplami == bolen_toplami

def bolen_bul(sayi):
    asal_bolenler = []
    for i in range(2, sayi):
        if sayi % i == 0 and asal_mi(i):
            asal_bolenler.append(i)
    return asal_bolenler

def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

try:
    sayi = int(input("Bir sayı giriniz: "))
    if smith_mi(sayi):
        print(f"{sayi} sayısı bir Smith sayıdır!")
    else:
        print(f"{sayi} sayısı bir Smith sayı değildir!")
except ValueError:
    print("Lütfen geçerli bir tam sayı giriniz!")