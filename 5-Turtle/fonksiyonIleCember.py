import math
import turtle


def turtle_olustur():
    tospik = turtle.Turtle()

    print(tospik)
    return tospik


def poligon(t, uzunluk, kenar_sayisi):
    aci = 360 / kenar_sayisi

    for i in range(kenar_sayisi):
        t.fd(uzunluk)
        t.lt(aci)


# Şimdi bir cember çizen bir fonksiyon yazıcaz
# Bu fonksiyonun parametreleri : kaplumbağa(t), yarıçap(r). 50 kenarlı

def cember(t, r):
    """
    :param t: turtle nesnesi
    :param r: yarı çap (int)
    : return = yok
    """
    cevre = 2 * math.pi * r
    n = int(cevre /0.5)
    uzunluk = cevre / n  # = kenar
    print(n)
    poligon(t, uzunluk, n)


tospik = turtle_olustur()
cember(tospik, 100)

turtle.mainloop()
