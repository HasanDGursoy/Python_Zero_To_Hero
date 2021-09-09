# Soru 1 :
# Aşşağıdaki gibi bir fonksiyon yazın. Adı 'tuple_yarat' olsun.
# Fonksiyon önce içinde 1 den 10 a kadar değerlerin olduğu bir tuple yaratsın.
# Ardından bu Tuple 11 den 20 ye kadar sayıları ve tuple'ın son halini dönsün.

# İpuçları
# Tuple Immutable dır . O tuple'a nasıl yeni eleman eklenir ?
# for döngüsü ve range() kullanın .

def tuple_yarat(t):
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    for i in range(11, 21):
        yeni_tup = tup + (i,)  # 1 elemanlı tuple böyle yazılır.
        tup = yeni_tup
    return tup


# Soru 2:
# Parametre olarak verilen bir Tuple'ı string e dönüştüren ve bu String'i geri dönen bir fonksiyon yazın.
# Adı tuple_to_string olsun

# ipucu : join()

def tuple_to_string(tup):
    metin = ''.join(tup)
    return metin


# Soru 3 :
# Parametre olarak bir String'i önce liste Sonrada Tuple'a dönüştüren bir fonksiyon yazın.
# İpuçları
# sadece list() ve tuple() kullanın

def string_to_list_to_tuple(t):
    t = list(t)
    t = tuple(t)

    return t


# Soru 4:
# Parametre olarak bir Tuple ve bir index alan bir fonksiyon yazın.
# Fonksiyon, verilen index'te yer alan elemanın tüm Tuple içinde kaç sefer yer aldığını bize dönsün.

# ipucu count()

def kac_kere_geciyor(tup, index):
    deger = tup[index]

    return tup.count(deger)


t = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)
i = 1
deger = kac_kere_geciyor(t, i)
print(deger)

# Soru 5 :
# tup = ('a','b','c','d','e','f','g','h','i',j)
# tuple' ını slicing antremanı yap

tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(tup[4:8])
print(tup[:5])
print(tup[::])
print(tup[-2:])
print(tup[-4:])
print(tup[2:8:2])
print(tup[::3])
print(tup[9:3:-1])
print(tup[::-1])
print(tup[::-2])
