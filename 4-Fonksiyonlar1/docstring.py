# Fonksiyon hakkında yardım alalım
# help den başka yardım alma şeklide var mesela cube? da diyebiliriz.
import math


def kare_hesapla(deger):
    deger = deger **2
    print(deger)

kare_hesapla(15)

def ustel(sayi,ust):

    # 3 tane Çift tırnak koyunca docstring haline gelir sadece okunur çalışmaz.
    """
     Bu fonksiyon üstel hesaplama yapar.
    :param sayi: integer deger
    :param ust: integer deger
    :return:
    """
    ustel_hesapla = math.pow(sayi,ust)
    return ustel_hesapla


# math.pow docstring görelim
help(math.pow)

# Pythonda nesnelerin hazır methodların ve attribute ların özellikleri vardır ve bunlara kısa yoldan erişilebilir.

print(ustel.__doc__)

# Pythonda built-in(hazır)  olan iki alt tire(__) ile erişilen metod veya attribute'lara "dunder" denir.
# dunder : double underscore

# Yarattıgımız ustel fonsiyonunun hangi modülde oldugunu görebilmek için
print(ustel.__module__)

def inp ():
    isim  = input("Lütfen İsminizi giriniz : ")

    print("Adınız : {0}".format(isim))

inp()






