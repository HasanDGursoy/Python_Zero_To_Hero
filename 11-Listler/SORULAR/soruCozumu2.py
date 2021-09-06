# SORU - 4
# Parametre olarak liste alsın.Adı 'karaler' olsun
# Fonksiyonumuz listedeki her bir elemanın karesini hesaplayacak ve yeni bir listeye ekleyecek.
# Sonuçta yeni parametre olarak gelen listeki elemanların karesini tutan yeni bir liste vericek.

def kareler(liste):
    yeni_liste = []

    for i in liste:
        yeni_liste.append(i ** 2)

    return yeni_liste


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d = kareler(liste)
print(d)


# SORU - 5 :
# Parametre olarak liste alsın. Adı 'kareler_toplamı' olsun
# Fonksyonumuz listenin başından başlayarak elemanların karelerini alacak.
# Bu kareleri toplayarak yeni bir liste oluşturcak oluşan yeni listenin her bir elemanı parametre olarak
# gelen listedeki o index'e kadar kareler toplamı olacak.

# Yani, yeni listedeki 4.eleman, gelen listedeki 1-2-3-4. elemanların kareleri toplamı olacak.

def kareler_toplami(liste):
    yeni_liste = kareler(liste)

    baska_liste = []
    deger_tutucu = 0
    for i, deger in enumerate(yeni_liste):
        deger_tutucu += deger
        baska_liste.append(deger_tutucu)

    return baska_liste


print(kareler_toplami(liste))


# SORU - 6
# Listenin tek indexlerini(1,3,5) toplamı ile çift indexleri (0,2,4) toplamı arasındaki farkı veren bir fonksiyon yazınız.
# Adı 'tek_cift_index_farki' olsun.
def toplam(liste):
    toplam = 0
    for i in liste:
        toplam = toplam + i

    return toplam


def tek_cift_index_farki(liste):
    tekler = liste[1::2]
    ciftler = liste[0::2]

    tekler_toplami = toplam(tekler)
    ciftler_toplami = toplam(ciftler)

    result = tekler_toplami - ciftler_toplami
    return result


print(tek_cift_index_farki(liste))


# SORU - 7
# Parametre olarak kendisine verilen listeyi kırpan bir fonksiyon yazın.Kırpma işlemi dizinin ilk ve son elemanını silmek demektir.
# Fonksiyonumuzun adı 'kipran' olsun ve kendisine verilen parametreyi yerinde değiştirsin.

def kirpan(liste):

    # ilk eleman silmek için
    liste.pop(0)

    # son eleman silmek için
    liste.pop(0)

















