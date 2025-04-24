#verilen decimal sayıyı binary değere çeviren programı yazınız!

def BinaryDegerBul(sayi):
    binary = []
    while sayi >= 2:
        kalan = sayi % 2
        binary.append(kalan)
        sayi = sayi // 2
    binary.append(sayi) 
    binary.reverse()    
    for bit in binary:
        print(bit, end="")  
    print()  

sayi = int(input("Sayi giriniz: "))
BinaryDegerBul(sayi)
