# BREAK  - DÖNGÜDEN ÇIKIŞ

# Verilen bir metnin harflerini yazalım.
# Harfleri yazarken, eğer boşluk karakteri görürsek döngüden çıkalım.

metin = input("Lütfen bir metin giriniz : ")

for harf in metin:

    if harf == " ":
        break
    print(harf)

# 30 dan 100 e kadar yazdırcaz.
for i in range(30, 100, 1):

    if i % 11 == 0:
        print(i)
        break
