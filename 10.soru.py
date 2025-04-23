#Girilen sayının kaç basamaklı olduğunu gösteren program !


number=input("Enter a number:")
number=int(number)

counter=0
temp=number
while temp!=0:

    temp=temp//10
    counter+=1
    
    

print(f"{number} sayisi {counter} basamaklidir!")
