# SORU - 6

# Verilen iki sözlüğü içinde key'leri aynı olan elemanlarının değerlerini toplayan bir fonksiyon yazın.
# Eğer key ikisindede ortak değilse almasın, sadece ortak keyleri alsın.
# Fonksiyonun adı 'ayni_key_toplamlari' olsun

# ipuçları
# Parametrelerin ikisininde sözlük olmasını kontrol edin
# değilse hata fırlatın
# kontrol için type yerine bu sefer (isinstance) kullanın
# sözlüklerin uzunluklarının aynı olmasını kontrol edin
# değilse hata fırlatın.

def ayni_key_toplamlari(d1, d2):
    toplam = {}

    if not isinstance(d1,dict) or not isinstance(d2,dict):
        raise Exception('Parametrelerin ikisi de sözlük olmalı')

    if len(d1) != len(d2):
        raise Exception('Sözlüklerin uzunluğu aynı olmalı')

    for key in d1 :

        if key in d2:

            toplam[key] = d1[key] + d2[key]

    return toplam




d1 = {'a': 10,'b':30,'c':50}
d2 = {'a':40,'b':60,'d':90}

deger=ayni_key_toplamlari(d1,d2)
print(deger)

print()
print()

# SORU - 7:
# Soru 6'daki fonksiyonu biraz daha geliştirelim
# Fonksiyonumuz aynı şekilde
# Verilen iki sözlüğü içinde keyleri aynı olan elemanların değerlerini toplasın
# Eğer key ikisnde ortak değilse hangisi varsa onu alsın.
# yani ortak elemanları toplam değer olarak, ayrık elemanları kendi değerleri ile döndürsün.
# Adı 'ayni_key_toplamlari_farkli_key_kendileri' olsun.

def ayni_key_toplamları_farkli_key_kendileri(d1,d2):

    if not isinstance(d1,dict) or not isinstance(d2,dict):
        raise Exception('Parametrelerin ikisi de sözlük olmalı')

    if len(d1) != len(d2):
        raise Exception('Sözlüklerin uzunluğu aynı olmalı')

    sozluk = {}

    for key in d1 :
        if key in d2:
            sozluk[key] = d1[key] + d2[key]

        else:
            sozluk[key] = d1
    for key in d2:
        if key not in d1:
            sozluk[key] = d2

    return sozluk

# SORU - 8
# Verilen bir dict'in içindeki tek index'li elemanları silip geriye sadece çift indexli elemanların olduğu dict'i döndürsün.
# Adı 'tekleri_sil'
# ipuçları
    # parametre olarak gelen orjinal dict'e dokunmayın.
    # döngü için items()
    # index içn enumarate()

def tekleri_sil(d1):

    d = {}

    for index,item in enumerate(d.items()):

        key = item[0]
        value = item[1]

        if index %2 ==0:
            d[key] = value # tabiki bunun yerine d.update({item}) da diyebilirdik :D

    return d

# SORU - 9
# Parametre olarak iki liste alan bir fonksiyon yazın.Fonksiyonuzun adı 'listeleri_sozluk_yap'
# Fonksiyon ilk listedeki elemanarı key, ikinci listedeki elemanları value yaparak ikisinden bir dict üretsin


def listeleri_sozluk_yap(list1,list2):

    sozluk = {}

    for i, value in enumerate(list1):

        sozluk[value] = list2[i]



    print(sozluk)


l1= ['ad','soyad','yas','cinsiyet']
l2 = ['john','doe',100,'erkek']

listeleri_sozluk_yap(l1,l2)

# SORU - 10
# Keyleri harf ve sayı olarak karışık olan bir sözlük düşünün.
# Yazacağımız fonksiyon, sadece harf olan keyleri bıraksın, diğerlerini silsin.Yani sadece alfanumerik olan keyli  elemanları alsın.
# Adı 'alfanumerik' olsun.

# İpuçları
    # Parametre olarak gelen orjinal dict'i değiştirin (yerinde : inplace)
    # İki döngü olsun
    # Döngüler için keys()
    # silme için pop()
    # alfanumerikmi diye bakmak için str.isalpha()
        # dikkat isalpha() bir string (str) fonksiyonudur.


def alfanumerik(dict):

    silinecek_seyler = []

    for key in dict.keys():

        if not str(key).isalpha():

            silinecek_seyler.append(key)

    for key in silinecek_seyler:

        if key in dict.keys():
            dict.pop(key)




    return dict



bos_sozluk = {'a':'A','b':'B',2:200,'d':'D',5:300,'f':'F',1:50}

deger = alfanumerik(bos_sozluk)