# Klavyeden girilen 20 adet sayıdan tek olanların toplamının çift olanların toplamına olan oranı!!

tekSayilar=[]
ciftSayilar=[]

for i in range(20):
    number=int(input("sayi gir:"))
    if number%2==0:
        ciftSayilar.append(number)
    else:
        tekSayilar.append(number)

print(f"Tek sayilarin toplaminin , cift sayilarin toplamina orani=% {(sum(tekSayilar)/sum(ciftSayilar))*100}")



