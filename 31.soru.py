# Kullanıcıdan 20 adet sayı alıp standart sapmasını hesaplayan programı yazınız.

def sapma_Hesapla(veriler):
    ortalama=sum(veriler)/ len(veriler)
    farkToplami= [(veri-ortalama)**2 for veri in veriler]
    return (sum(farkToplami) / len(veriler))** 0.5


veriList=[]
sayac=0
while sayac < 20:
    veri=input("Sayi giriniz:")
    veri=int(veri)
    veriList.append(veri)
    sayac+=1

standart_sapma=sapma_Hesapla(veriList)
print(f"Verilenizin standart sapması : {standart_sapma:.3f}")