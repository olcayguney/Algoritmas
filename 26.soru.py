def indeksHesap(kilo, boy):
    indeks = kilo / (boy ** 2)
    print(f"Vücut Kitle İndeksiniz = {indeks:.2f}")
    indeksYorum(indeks)

def indeksYorum(indeks):
    if indeks < 18.5:
        print("Durum: Zayif")
    elif 18.5 <= indeks < 25:
        print("Durum: Normal")
    elif 25 <= indeks < 30:
        print("Durum: Kilolu")
    else:
        print("Durum: Obez")

# Kullanıcıdan veri alma
try:
    kilo = float(input("Kilonuzu (kg) cinsinden giriniz: "))
    boy = float(input("Boyunuzu (metre) cinsinden giriniz: "))
    indeksHesap(kilo, boy)
except ValueError:
    print("Lütfen geçerli bir sayi giriniz.")
