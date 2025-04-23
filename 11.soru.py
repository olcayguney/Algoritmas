# girilen 3 basamaklı bir sayının basamakları küpleri toplamının girilen sayıya eşit olup olmadığını bulan program!!

def hesapla(x):
    temp = 0
    for i in x:
        i = int(i) ** 3  # küp alınıyor
        temp += i
    return int(x) == temp


sayi = input("3 basamaklı bir sayı giriniz: ")

# Girdi doğrulaması
if not sayi.isdigit():
    print("Hatalı giriş: Lütfen sadece rakamlardan oluşan bir değer giriniz.")
elif len(sayi) != 3:
    print("Lütfen sadece 3 basamaklı bir sayı giriniz!")
else:
    if hesapla(sayi):
        print("Sayınızın basamaklarının küpleri toplamı sayınıza eşit!")
    else:
        print("Sayınızın basamaklarının küpleri toplamı sayınıza eşit değil!")
