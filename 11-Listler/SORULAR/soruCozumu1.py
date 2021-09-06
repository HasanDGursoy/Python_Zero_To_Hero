# SORU  - 1
# Parametre olarak bir liste alan bir fonksiyon yazın.Adı toplam olsun.
# Bu fonksiyon verilen listenin tüm elemanlarını toplasın ve geriye genel toplam döndürsün.

def toplam(liste):
    toplam = 0
    for i in liste:
        toplam = toplam + i

    print(toplam)


toplam_listesi = [1, 2, 3, 4, 5]
toplam(toplam_listesi)
print("============================= SORU - 2 ===================================================")


# SORU - 2
# Parametre olarak iç içe bir liste alan bir fonksiyon yazın ve ismi 'iki_seviyeli_toplam' olsun
# Fonksiyon kendisine verilen matrisi toplasın

def iki_seviyeli_toplam(matris):
    c = 0
    if type(matris) == list:

        for i in matris:

            for j in i:
                c = c + j
    print(c)


matris = [
    [10, 10, 10],
    [10, 10, 10],
    [10, 10, 10]
]
iki_seviyeli_toplam(matris)


# SORU -  3

# Soru 2'de yazdığımız fonksiyon sadece 2seviyeli iç içe liste alabiliyordu.
# Şimdi bunu jenerik bir hale getirelim ve her seviyeye iç liste toplayabilsin.
# İsmi 'ic_ice_toplam' olsun.
# ipucu : Recursive
# Sonsuza kadar bütün listeleri topyalabilir hale geldi.

def ic_ice_toplam(dizi):
    toplam = 0

    for eleman in dizi:

        if type(eleman) == int:
            toplam += eleman

        elif type(eleman) == list:

            # burdaki olay eğer fonksiyona verilen deger liste ise recursion yapıp
            # listenin elemanlarına ulaşana kadar yani ilk if' deki int değerine eşit olana kadar fonksiyonu çağır dedik.

            toplam += ic_ice_toplam(eleman)
