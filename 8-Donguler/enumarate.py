# ENUMARATE KAVRAMI
# Enumarate sayesinde index alabiliyoruz.

metin = input("Lütfen bir metin giriniz : ")

yeni_metin = ""

for index, harf in enumerate(metin):

    # harfi ve "-" karakterlerini yeni metne ekle

    yeni_metin += harf
    if index < len(metin) - 1:
        yeni_metin += "-"

print(yeni_metin)


# 10 dan başlayıp 100'e kadar 5'er saydığımızı farzedelim
# acaba 6.sıradaki sayı kaçtır. index = 5 demek.

aralik = range(10,101,5)

for index,sayi in enumerate(aralik):
    if index == 5:
        print(sayi)

