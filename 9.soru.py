# Kullanıcıdan saniye türünden bir süre alarak bunu saat , dakika ve saniyeye 
# döndüren programı tasarlayınız.

x=int(input("Süreyi giriniz:"))

saniye=x%60
dakika=(x//60)%60
saat=x//3600
print(f"{saat} saat, {dakika} dakika, {saniye} saniye")