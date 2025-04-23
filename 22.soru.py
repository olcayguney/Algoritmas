# Girilen sayının Zengin (Abundent) sayı olup olmadığını bulan programı yazınız.
# Abundent sayi : Bölenlerinin toplamı kendinden büyük olan sayılardır.
# Deficient sayi : Bölenlerinin toplamı kendinden küçük olan sayılardır.

def bolenListBul(sayi):
    bolenList=[]
    for i in range(1,sayi//2+1,1):
        if sayi%i==0:
            bolenList.append(i)
    return sorted(set(bolenList))  # Bu kısımda set ile tekrar eden değerleri silerseniz. sorted ile ise sıralarsınız.

def zenginMi(sayi):

    print(f"Sayinizin bolenleri : {bolenListBul(sayi)}")
    if sum(bolenListBul(sayi))>sayi:
        print(f" {sayi} sayisi abundent sayidir!!")
    else:
        print(f"{sayi} sayisi güçsüz sayidir!!")


num=int(input("Sayi giriniz:"))
zenginMi(num)
