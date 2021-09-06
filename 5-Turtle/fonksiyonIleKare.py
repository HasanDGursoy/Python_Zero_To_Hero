import turtle


def create_turtle():
    tospik = turtle.Turtle()
    print(tospik)
    return tospik


def kare(t, uzunluk):
    """
    Kamplumbaganın ne kadar yürütceğini söylicez.
    :param t: turtle tipinde deger
    :param uzunluk: int tipinde deger
    :return:
    """
    for i in range(4):
        t.fd(uzunluk)
        t.lt(90)


tospik = create_turtle()

kare(tospik, 100)
kare(tospik, 200)
kare(tospik, 300)

tospik.clear()
# Şimdi araları dolduralım

# 300 - 100 = 200
# 10 seferde doldurmak için 200 / 10 = 20 pixel

for i in range (10):
    kare(tospik,100 + i* 20)

tospik.clear()

# Fonksiyon kullanarak Poligon çizelim

def poligon(turtle,uzunluk,kenar_sayisi):

    """
    Kaplumbağa ile poligon çizen bir fonksiyon çizelim

    :param turtle: turtle nesnesi
    :param uzunluk: int
    :param kenar_sayisi: n
    :return:
    """
    # Dönüş derecesi hesapla
    aci = 360/ kenar_sayisi

    for i in range(kenar_sayisi):
        turtle.fd(uzunluk)
        turtle.lt(aci)

poligon(tospik,100,6)
poligon(tospik,100,10)
# İsimlendirilmiş parametrelere değer atayarak da kullanabiliyoruz.
poligon(tospik,uzunluk=15,kenar_sayisi=20)

turtle.mainloop()

