# KOMPOZİSYON - Fonksiyonları Beraber Kullanma

# Fonksiyonel Programlama
# Yapılacak işleri küçük parçalara bölmek ve onları kendi fonksiyonlarına vermek.

# örn = Diyelim ki elimizde iki nokta var
# Bu iki noktayı birleştiren doğru parçasını yarıçap kabul edelim
# Bu yarı çapa sahip dairenin alanını hesaplayalım

import math


def alan(yaricap):
    return math.pi * yaricap ** 2


def uzaklik(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    kareler_toplami = dx ** 2 + dy ** 2
    return math.sqrt(kareler_toplami)


def iki_noktadan_gecen_daire_alani(x1, y1, x2, y2):
    """
    Yarı çapı verilen iki nokta arası olan bir dairenin alanını hesaplar
    :param x1: int, birinci noktanın x kordinatı
    :param y1: int
    :param x2: int
    :param y2: int
    :return: dairenin alani  (int)
    """
    # yarıçap hesaplayalım
    r = uzaklik(x1, y1, x2, y2)

    # alan hesapla
    alan_hesapla = alan(r)
    print(alan_hesapla)

    return alan_hesapla


iki_noktadan_gecen_daire_alani(1, 6, 4, 10)


# BOOL FONKSİYONLAR
# Çoğu zaman bir karar verirken doğru yada yanlış olduğunu bilmemiz gerekir..
# Bu durum için doğrumu yoksa yanlış mı, sonucunu veren fonksiyonlar tanımlarız.
# True ya da False döner

# Sayı tek mi çift mi -> x %2 == 0 : çift

def cift(x):
    return x % 2 == 0


# Tek mi fonksiyonu
def tek_mi(x):
    return x % 2 == 1


cifts = cift(15)
print(cifts)
teks = tek_mi(15)
print(teks)
