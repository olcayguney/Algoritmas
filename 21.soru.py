

def fonk(minValue,maxLimit):
    temp=minValue
    
    for i in range(maxLimit-minValue):
        sumTemp=0
        for j in range(1,temp,1):
            if temp%j==0:
                sumTemp+=j
        if sumTemp==temp:
            print(f"{temp} Sayisi Mukemmel Sayidir!")
       
        temp+=1
        
        






num1, num2 = map(int, input("Hangi araliklari gireceksiniz : ").split())
fonk(num1,num2)
