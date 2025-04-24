# ax^2 + bx + c = 0 formatında a, b ve c değerlerini kullanıcıdan alan ve köklerini bulan program.

import math

def delta_bul(a, b, c):
    return (b**2) - (4 * a * c)

def kok_bul(a, b, c):
    delta = delta_bul(a, b, c)
    if delta < 0:
        print("Denklemin reel kökü yoktur (karmaşık kökler vardır).")
    elif delta == 0:
        kok = -b / (2 * a)
        print(f"Denklemin tek kökü vardır: {kok:.2f}")
    else:
        kok1 = (-b + math.sqrt(delta)) / (2 * a)
        kok2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Denklemin kökleri: {kok1:.2f} ve {kok2:.2f}")

try:
    a, b, c = map(float, input("a, b ve c değerlerini aralarında boşluk olacak şekilde giriniz: ").split())
    if a == 0:
        print("Bu bir ikinci dereceden denklem değildir (a sıfır olamaz).")
    else:
        kok_bul(a, b, c)
except ValueError:
    print("Lütfen geçerli sayılar giriniz!")