def besinKuvvetiMi(sayi):
    while sayi % 5 ==0:
        sayi=sayi//5
    if sayi==1:
        return True
    else:
        return False

num=int(input("sayi giriniz:"))

if besinKuvvetiMi(num):
    print("evet")

else:
    print("hayir")
