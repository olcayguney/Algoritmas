# Klavyeden girilen bir sayinin pozitif mi negatif mi olduğunu bulma

def isaretBul(sayi):
    if sayi < 0:
        print("negatif")
    elif sayi>0:
        print("pozitif")
    else:
        print("sayiniz 0 ' a eşittir")

num=int(input("sayi giriniz:"))
isaretBul(num)