# SORU - 1
# kelimeler.txt dosyasını okuyan ve burdaki kelimelerden bir dict yaratan bir fonksiyon yazın.
# Fonksiyon sadece 19 karakter ve üstü olan kelimeleri alsın.
# Dictionary'nin key'i kelime olacak  ve değeride kelimenin harf sayısı yani uzunluğu olacak.
# Fonksiyonun adı = 'kelimeler_sozlugu' olsun ve yarattığı Dict dönsün.

def kelimeler_sozlugu():
    file = open('kelimeler (1).txt')

    new_dict = dict()

    for key in file:

        kelime_dizisi = key.split()
        kelime = kelime_dizisi[0]
        if not kelime in new_dict:
            if len(kelime) >= 19:
                new_dict[kelime] = len(kelime)
    return new_dict


print(kelimeler_sozlugu())

print()
print("========================================================================")
print()


# SORU - 2 :
# kelimeler.txt dosyasını okuyan ve buradaki kelimelerden bir dictionary yaratan bir fonksiyon yazın.
# sadece 19 kelime ve üstünü alsın.
# Dict'in key'i karakter karakter sayısı (uzunluk) olacak ve değeri bu karakter sayısına sahip kelimeleri içeren bir list olacak.
# Fonksiyonun adı : 'uzunluk_kelimeler' olsun ve yarattığı Dictionaryı dönsün.

def uzunluk_kelimeleri():
    file = open('kelimeler (1).txt')

    bos_dict = dict()

    for kelimeler in file:

        kelime_dizisi = kelimeler.split()
        kelime = kelime_dizisi[0]

        if len(kelime) >= 19:
            if not len(kelime) in bos_dict:

                bos_dict[len(kelime)] = [kelime]
            else:
                bos_dict[len(kelime)].append(kelime)
    return bos_dict


deger = uzunluk_kelimeleri()
print(deger)

print()
print("========================================================================")
print()


# SORU - 3
# isimleri arac_yarat_1, arac_yarat_2,arac_yarat_3,arac_yarat_4 olan 4 fonksiyon yazın.
# Bu fonksiyonlar aşşağıdaki gibi bir dict yaratsın ve dict'in adı araç olsun.

# 1.YOL

def arac_yarat_1():
    arac = {}
    arac['marka'] = 'Ford'
    arac['model'] = 'Mustang'
    arac['yıl'] = 1964
    arac['renk'] = 'Red'
    arac['fiyat'] = 300000
    arac['km'] = 89000
    arac['motor'] = 1.6

    return arac


# 2.YOL

def arac_yarat_2():
    arac = dict()
    arac['marka'] = 'Ford'
    arac['model'] = 'Mustang'
    arac['yıl'] = 1964
    arac['renk'] = 'Red'
    arac['fiyat'] = 300000
    arac['km'] = 89000
    arac['motor'] = 1.6
    return arac


print(arac_yarat_2())


# 3.YOL

def arac_yarat_3():
    arac = dict()
    arac.update(
        {'marka': 'Ford',
         'model': 'Mustang',
         'yıl': 1964,
         'renk': 'Red',
         'fiyat': 300000,
         'km': 89000,
         'motor': 1.6}
    )
    return arac


# 4. YOL

def arac_yarat_4():
    arac = dict(
        {'marka': 'Ford',
         'model': 'Mustang',
         'yıl': 1964,
         'renk': 'Red',
         'fiyat': 300000,
         'km': 89000,
         'motor': 1.6}
    )

print()
print("========================================================================")
print()

# SORU - 4
# Adı yeni_arac_yarat olan bir fonksiyon yazın. Bu fonksiyon soru 3'teki fonksiyonlardan birini çağırsın ve arac sözlüğü alsın.
# Sonra arac sözlüğünün elemanlarını bir döngü ve update() kullanarak başka bir sözlüğe kopyalasın.
#
























