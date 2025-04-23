# 10 ile 1000 sayılarının arasında tam kare olan sayıları bulan program .

import math

tam_kareler = []

for i in range(10, 1001):
    kok = math.sqrt(i)  # sqrt karekök ' ü ifade yani  sayi üzeri (1/2)' de diyebiliriz
    if kok.is_integer():   # sayı bir integer' a yani tam sayıya eşitse tam karedir diyebiliriz.
        tam_kareler.append(i)

print(tam_kareler)


