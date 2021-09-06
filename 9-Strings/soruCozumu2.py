# SORU - 4 : Metiminiz "Pazartesi Salı Çarşamba Perşembe Cuma" olsun
#          : Bu metin üzerinde dilimle kullanarak aşşağıdaki sorulara cevap veriniz.
gunler = "Pazartesi Salı Çarşamba Perşembe Cuma"
"""
* ilk 3 karakteri bulunuz.
* 7.karater ile 10. karakter (dahil) arasını bulunuz.
* 2.karakterden, 12. karaktere kadar olanları bulunuz.
* 3,4 ve 5. index'li karakterleri bulunuz.

"""
# 1. Çözüm
print(gunler[0:3])
# 2. Çözüm
print(gunler[7:11])
# 3. Çözüm
print(gunler[2:12])
# 4. Çözüm
print(gunler[3:6])

# SORU - 5 : Metnimiz "Pazartesi Salı Çarşamba Perşembe Cuma" olsun
#          : Bu metin üzerinde slicing kullanarak cevaplayın.

"""
1. karakterden 7. karaktere kadar olan harfleri ikişer atlayarak bulunuz.
3. karakterden 20. karaktere kadar olan harfleri üçer atlayarak bulunuz.
* çift indexli karakterleri bulunuz.
* tek indexli karakterleri bulunuz.

"""
# 1.Çözüm
print(gunler[1:7:2])
# 2.Çözüm
print(gunler[3:20:3])
# 3.Çözüm
print(gunler[::2])
# 4. Çözüm
print(gunler[1::2])

# SORU - 6 : Metnimiz 'Pazartesi Salı Çarşamba' olsun
#          : Slicing kullanarak aşşağıdaki soruları cevaplayın.

"""
* Son karakteri bulunuz.
* Sondan 5. karakteri bulunuz.
* Son 3 karakteri bulunuz.
* Metni tersten yazdırınız.

"""
haftanin_yarisi = "Pazartesi Salı Çarşamba"
# 1. Çözüm
print(haftanin_yarisi[-1])
# 2. Çözüm
print(haftanin_yarisi[-5])
# 3. Çözüm
print(haftanin_yarisi[-1:-4:-1])
# 4. Çözüm
print(haftanin_yarisi[::-1])

