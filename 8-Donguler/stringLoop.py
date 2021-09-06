metin = "Python"

for harf in metin:
    print(harf)

metin = input("Lütfen bir metin giriniz : ")
yeni_metin=""
for harf in metin :
    # harfi ve "-" karakterlerini yeni metne ekle

    yeni_metin +=harf+"-"
print(yeni_metin)

# LENG KAVRAMI
# Python da yapı itibarı ile dizi olan tipler (str,list..) için uzunluk len fonksiyonu ile bulunur.

len("Python")
dizi = [1,2,3,"A","B"]
print(len(dizi))

metin = input("Lüfen bir metin giriniz : ")

for i in metin:
    print(i)