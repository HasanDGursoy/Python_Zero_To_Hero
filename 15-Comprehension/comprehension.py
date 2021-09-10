# COMPREHENİSON
# Pythonda dizi tipinde(sequence) değişkenler üzerinde kolayca döngü kurmamızı sağlayan yapılardır.

# Alıştırma
# 1-10 arası sayıların karelerini içeren bir liste yapalım.

kareler = []
for i in range(11):
    kareler.append(i ** 2)
print(kareler)

# Comprehension ile yapalım

kareler_comp = [i ** 2 for i in range(11)]
print(kareler_comp)

harf_ekle = [i * 3 for i in range(23)]
print(harf_ekle)

# Alıştırma :
# 1-7 kadar olan sayıların küplerini ekrana yazalım :

# önce klasik yöntem

kup = []

for i in range(1, 8):
    kup.append(pow(i, 3))

print(kup)

# Comprehension ile yapalım birde

kupler_comp = [i ** 3 for i in range(8)]
print(kupler_comp)

# Alıştırma :

# 'lorem ipsum' ifadesinin harflerini büyük harfler yapıp bir listeye ekleyelim

# Klasik Yöntem
buyuk = []
text = 'lorem ipsum'

for t in text:
    buyuk.append(t.upper())

print(buyuk)

# comprehension ile yapalım.

buyuk_comp = [t.upper()
              for t in text]
print(buyuk_comp)

## DİCTİONARY ÜZERİNDE COMPREHENSİON ÇALIŞTIRMAK

programlama_dilleri = ['Python', 'Java', 'JavaScript', 'C#']
cikis_yillari = [1989, 1995, 1995, 2000]

diller_yillar = {}

for dil, yil in zip(programlama_dilleri, cikis_yillari):
    diller_yillar[dil] = yil

# Comprehension ile yapalım

dil_yil = {dil: yil
           for dil, yil in zip(programlama_dilleri, cikis_yillari)
           }
print(dil_yil)

# 'Papatya' kelimesinin harflerini bir kümede gösterelim

metin = 'papatya'

# normal
kume = set()

for letter in metin:
    kume.add(letter)

print(kume)

# comprehension

kume_comp = {harf for harf in metin}
