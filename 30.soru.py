# Kullanıcıdan gerekli bilgileri alarak Fizikteki Atış konusunun 
# sorularını çözen programı tasarlayınız.

import math
yer_cekimi = 9.81


atis_hizi = float(input("Atiş hizini giriniz (m/s): "))
yukseklik = float(input("Yüksekliği giriniz (m): "))
atis_acisi = float(input("Atiş açisini giriniz (derece): "))

atis_acisi_radyan = math.radians(atis_acisi)

x_ekseni_hizi = atis_hizi * math.cos(atis_acisi_radyan)
y_ekseni_hizi = atis_hizi * math.sin(atis_acisi_radyan)

havada_kalma_suresi = (2 * y_ekseni_hizi) / yer_cekimi

maksimum_yukseklik = (y_ekseni_hizi**2) / (2 * yer_cekimi)

maksimum_menzil = havada_kalma_suresi * x_ekseni_hizi

print(f"Havada kalma süresi: {havada_kalma_suresi:.2f} saniye")
print(f"Maksimum yükseklik: {maksimum_yukseklik:.2f} metre")
print(f"Maksimum yatay mesafe: {maksimum_menzil:.2f} metre")