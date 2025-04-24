asalBolenTut=[]

def maxBul(x):
    max=x[0]
    for i in range(1,len(x),1):
        if max < x[i]:
            max=x[i]
    x.remove(max)
    return max
        

def bolenBul(number):
    for i in range(2,number,1):
        if number%i==0:
            if asalMi(i):
                asalBolenTut.append(i)


def asalMi(x):
    for i in range(2,x,1):
        if x % i ==0:
            return False
        
    return True


def fizzBuzz(number):
    bolenBul(number)
    
    if len(asalBolenTut) < 2:
        print("Yeterli asal bölen yok.")
        return
    
    x=maxBul(asalBolenTut)
    y=maxBul(asalBolenTut)
    for i in range(1, number):
        if i % (x*y)==0:
            print("Fizz&Buzz")
        elif i % x==0:
            print("Buzz")
        elif i % y==0:
            print("Fizz")
        else:
            print(i)

    
temp=input("Sayi Giriniz:")
temp=int(temp)

fizzBuzz(temp)
