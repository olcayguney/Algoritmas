#   Girilen sayinin mükemmel sayi olup olmadığını bulan programı yazınız.
#   mükemmel sayi , kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayıdır.

def mukemmelMi(x):
    toplam = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            toplam += i
    return toplam == x

num = int(input("Bir sayi giriniz: "))

if mukemmelMi(num):
    print(f"{num} mükemmel bir sayidir!")
else:
    print(f"{num} mükemmel bir sayi değildir.")
