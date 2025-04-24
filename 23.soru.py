# 0-1000 arasında kullanıcıdan alınan sayıyı tahmin eden programı yazınız.

def tahminEt():
    alt = 0
    ust = 1000
    while alt <= ust:
        tahmin = (alt + ust) // 2
        cevap = input(f"Tuttuğunuz sayi {tahmin} mi? (evet/hayir): ")
        if cevap.lower() == "evet":
            print("Tahmin doğru! Sayi:", tahmin)
            return
        cevap = input(f"Tuttuğunuz sayi {tahmin}'den küçük mü? (evet/hayir): ")
        if cevap.lower() == "evet":
            ust = tahmin 
        else:
            alt = tahmin 
    print("Tahmin edilemedi.")




print("0-1000 arasinda bir sayi tuttunuz.")
tahminEt()


