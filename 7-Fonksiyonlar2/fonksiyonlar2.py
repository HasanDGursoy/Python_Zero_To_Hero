# ------ FONKSİYONLAR------#
"""
1.Fonksiyonlar çoğu zaman işlemlerini bitirdikden sonra geriye bir değer döndürür.
  Fonksiyonu çağıran yerde o değeri alır ve buna göre işlem yapar.
2.Fonksiyon eğer geriye değer döndürmüyorsa buna "VOİD" fonksiyon denir.
3.Geriye değer dönme --> "return"

"""
import math


def alan(yaricap):
    a = math.pi * yaricap ** 2
    return a


daire_alani = alan(4)
print(daire_alani)


# Yukarıidaki fonksiyonda a değişkenini kullanmak zorunda değiliz.

def alan(yaricap):
    return math.pi * yaricap ** 2


# bunu direk return e yazsak da oluyor.

daire_alani = alan(5)
print(daire_alani)


## ADIM ADIM GELİŞTİRME
# Kodlama yaparken herşeyi tek seferde düşünemeyiz ve yapamayız.
# Bu yüzden adım adım geliştirme üzerine yoğunlaşmamız lazım.
# Adım adım geliştirme, hata ayıklama(debug) için olmazsa olmaz bir kavramdır.
# Eğer programın her adımda neyi yaptığını debug edemezseniz o zaman herşeyi doğru yaptığından emin olmalısınız.
# ör. Diyelim ki iki nokta arasındaki mesafeyi hesaplamak istiyouz
# Noktalar -> (x1,y1) ve (x2,y2)

def uzaklik(x1, y1, x2, y2):
    # Önce x'ler arasındaki farkı hesapla
    dx = x2 - x1

    # sonra y'ler arasındaki farkı hesapla
    dy = y2 - y1

    # <---- DEBUG ---->
    # daha fazla devam etmeden bunları doğru hesapladığımızı kontrol edelim

    print("dx :", dx)
    print("dy : ", dy)

    # karelerin toplamını hesapla
    kareler_toplami = dx**2 + dy**2

    # <---- DEBUG ----->
    print("karelerin toplamı : ",kareler_toplami)

    return math.sqrt(kareler_toplami)




# Printlerle DEBUG yaptıgmız olaya : TDD (Test Driven Development)

kare_toplam =uzaklik(1,2,3,4)
print(kare_toplam)