# SORU - 1
"""
Ekrana yıldızlardan oluşmuş bir kare çizen fonksiyon yazın.
Fonksiyon parametre olarak karenin bir kenarında bulunan yıldız sayısını alsın.
Diyelim ki kullanıcı 5 olarak girdi sayıyı, ozaman karennin 5 satırı ve here satırdı 5 stünu (yıldız) olur.
Bunun için iç içe while döngüleri kullanalım.

"""

print("---------------------------------------------------------")


def kare_ciz(deger):
    for i in range(deger):
        kare = ""
        for j in range(deger):
            kare += "* "
        print(kare)


deger = int(input("Yıldız Sayısını Giriniz :"))
kare_ciz(deger)
print("---------------------------------------------------------")


# SORU - 2
# Yukarıdaki örneği while ile yapalım.

def kare_yildiz_while(deger):
    i = 0
    while i < deger:
        kare = ""
        j = 0
        while j < deger:
            kare += "* "
            j += 1
        i += 1
        print(kare)


kare_yildiz_while(deger)

print("---------------------------------------------------------")


# SORU - 3
# Ekrana yıldızlardan oluşmuş bir ikizkenar dik üçgen çizen bir fonksiyon yazın.
# Fonksiyon parametre olarak üçgenin dik bir kenarında bulunan yıldız sayısını alsın.

def dik_ikiz_kenar(deger):
    i = 0
    while i < deger:
        j = 0
        dik_ucgen = ""
        while j <= i:
            dik_ucgen += "* "
            j += 1
        print(dik_ucgen)
        i += 1


dik_ikiz_kenar(deger)
print("---------------------------------------------------------")


# SORU - 4
# Ekrana soru - 3 ün aynısını for ile yazdır.

def dik_ikiz_kenar_for(deger):
    for i in range(deger):
        ucgen = ""
        for j in range(i+1):
            ucgen += "* "
        print(ucgen)


dik_ikiz_kenar_for(deger)
