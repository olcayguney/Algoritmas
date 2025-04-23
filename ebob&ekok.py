def Ebob(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def Ekok(a,b):
    return (a*b)//Ebob(a,b)



num1=input("Enter ur first number:")
num1=int(num1)
num2=input("Enter ur second number:")
num2=int(num2)
if num1==0 or num2==0:
    print("the number can be zero")
else:
    print(f"EBOB({num1},{num2})={Ebob(num1,num2)}")
    print(f"EKOK({num1},{num2})={Ekok(num1,num2)}")

