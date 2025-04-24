# Binary olarak verilen sayının Decimal karşılığını bulan program.
def reversele(x):
    return x[::-1]

binaryNum=input("Binary degerinde sayinizi giriniz:")

sayac=0
temp=0
binaryNum=reversele(binaryNum)
for i in binaryNum:
    if int(i)==1:
        temp+=2**sayac
    sayac+=1

print(temp)

    

