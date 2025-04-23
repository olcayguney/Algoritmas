# Fibonacci serisinin programını yazınız.

"""def fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)


num=input("Enter the what do you want on calculations:")
num=int(num)

for i in range(num+1):
    print(f"f({i})={fibonacci(i)}")

#print(f"f({num})={fibonacci(num)}")  if you  want to  calculate just the entered number"""




num=input("Enter the what do you want on calculations:")
num=int(num)
nowTemp=0
nextTemp=1
sayac=2
result=0
while True:
    result=nowTemp+nextTemp
    nowTemp=nextTemp
    nextTemp=result
    print(f"f({sayac})={result}")
    sayac=sayac+1
    if sayac > num:
        break
    








