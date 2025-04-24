# Girilen 4 basamaklı sayının orijinal sayı olup olmadığını bulan programı yazınız.
# Orijinal sayı : 4 basamaklı sayının ilk 2 basamağı ile son 2 basamağının toplamının karesi kendisine eşit olan sayılar.

def orijinalMi(number):
    temp=int(number[:2])+int(number[2:])
    if int(number)==temp**2:
        print("Sayiniz orijinal sayidir!")
    else:
        print(f"sonuc = {temp**2}")
        print("sayiniz orijinal sayi degildir!")



sayi=input("4 Basamakli sayi giriniz:")
if len(sayi) != 4 or not sayi.isdigit():
    print("Lütfen geçerli bir sayi giriniz.")
else:
    orijinalMi(sayi)

