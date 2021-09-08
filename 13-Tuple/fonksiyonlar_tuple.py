# FONKSİYONLARIN DÖNÜŞ DEĞERİ OLARAK TUPLE'LAR

# Fonksiyonları işlerken farketmiş olabilirsiniz.Fonksiyonlar geriye sadece bir değer döner.
# Peki birden fazla değer dönmesi gerekse ne yapacağız.
# Cevap * Tuple *. Dönecek değerleri bir Tuple içine alırsak o zaman geriye sadece Tuple'i dönmemiz yeterli.
# Örneğin Python'un standart divmod() fonksiyonu iki parametre alır.
# İki parametre döndürür.

sonuc = divmod(23, 4)
print(sonuc)

# bölüm ve kalan'ı ayrı ayrı alalım.

bolum = sonuc[0]
kalan = sonuc[1]
print(bolum)
print(kalan)

bolum, kalan = divmod(23, 4)


# Alıştırma
# Parametre sayısı belli olmayan bir fonksiyon yazın.

def toplam_ve_carpim(*args):
    toplam = sum(args)

    carpim = 1
    for arg in args:
        carpim *= arg

    return (toplam, carpim)


toplam_ve_carpim(2, 3, 4, 5)

# *args yapısı aslında bir tuple'dır.

toplam, carpim = toplam_ve_carpim(2, 3, 4, 5, 6, 7, 8)
print(toplam, carpim)

# Alıştırma
# Parametre olarak bir tam sayı listesi alan ve bu listenin 'min, max ve aritmetik ortlama' değerlerni dönen bir fonksiyon.

# İpuçları
# ortalama(mean) fonksiyonu için 'statistics' yani istatistik paketini kullanın.
# modülü import etmek için --> import

import statistics


def basit_istatistik(liste):
    # min
    minumum = min(liste)

    # max
    maximum = max(liste)

    # ortalam
    ort = statistics.mean(liste)

    # return et --> tuple içinde paketleyerek (pack)

    return (minumum, maximum, ort)


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

deger = basit_istatistik(liste)
print(deger)

minumum,maximum,ortalama = basit_istatistik(liste)
print('min : ',minumum)
print('max : ',maximum)
print('ort : ',ortalama)