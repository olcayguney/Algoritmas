# verilen hazır listeden en büyük 6. sayıyı bulan programı yazınız.
import random

random_List=[]
for i in range(20):
    random_List.append(random.randint(1, 100))
print(random_List)

for i in range(20):
    minindex=i
    for j in range(i+1,20):
        if random_List[j] < random_List[minindex]:
            minindex=j
    
    random_List[i],random_List[minindex]=random_List[minindex],random_List[i]

            
print(random_List)

print(random_List[-6])


