# SORU - 4
# Verinlen bir listenin büyükten küçüğe sıralı olup olmadığını kontrol eden bir fonksiyon yazınız.
# Adı = azalan_sirali_mi olsun ve eğer liste büyükden küçüğe sıralı ise True , değilse false dönsün.
# Yapılacaklar
# 4 farklı yolla bu soruyu çözün.

# Yol 1:
# İç içe döngüler
# En az pythonic yöntem :S

def azalan_sirali_mi(liste):
    for i, eleman_1 in enumerate(liste):

        for j, eleman_2 in enumerate(liste):

            if j > i:

                if eleman_2 > eleman_1:
                    return False
    return True


dizi = [8, 7, 6, 5]
deger_tutucu = azalan_sirali_mi(dizi)
print(deger_tutucu)


# Yol 2 :
# Birdazdaha pythonic bir yöntem kullanalım.

def azalan_sirali_mi_2(liste):
    # baştan sona kadar git
    # her elemanı kendisinden sonraki ile karşılatır.
    # eğer fark negatif ise, o zaman azalmıyordur.

    for i in range(len(liste) - 1):

        if liste[i] - liste[i + 1] < 0:
            return False
    return True


dizi = [8, 7, 6, 5]
deger_tutucu = azalan_sirali_mi_2(dizi)
print(deger_tutucu)


# Yol 3 :
# Sıralı liste ile kontrol
# Pythonic kontrol yaklaşıyor bebeğim :D

def azalan_sirali_mi_3(liste):
    # yeni bir liste yarat
    sirali_liste = liste[:]

    # sirali listeyi büyükten küçüğe sırala
    sirali_liste.sort(reverse=True)

    if not liste == sirali_liste:
        return False
    else:
        return True


# İşte Geldi Beklenen YOL 4 YOL 4 YOL 4 :
# En pythonic ve fonksiyonel yol o bir efsane

def azalan_sirali_mi_4(liste):
    return sorted(liste, reverse=True) == liste

dizi = [8,7,6,5]
deger_tutucu = azalan_sirali_mi_4(dizi)
print(deger_tutucu)
