import random
listem=[1,2,3,4,5]

print(listem)

# listName.append(value)    APPEND
# Listenin **sonuna** komut içerisindeki değeri giriyor!
listem.append(77)
print(listem,"append")

# listName.insert(index,value)  INSERT
# Listenin girilen indexine girilen değeri giriyor!

listem.insert(1,88)
print(listem," insert")

# listName.remove(value)  REMOVE
# Komutun içerisindeki değeri listeden siliyor  
# !( Birden fazla var ise sadece ilk bulduğunu siler)

listem.append(88)
print(listem)
listem.remove(88)
print(listem," remove")




