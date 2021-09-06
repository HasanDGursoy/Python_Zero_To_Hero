# SORU - 9 :
# 1-50 arası kadar olan sayılar üzerinde dönen bir fonksiyon yazın.
# 3' ün katları için sayının kendisi yerine "Üj"
# 5' in katları için sayının kendisi yerine "Bej"
# 3 ve 5 ' in ortak katları için ise sayının kendisi yerine "ÜjBej" yazsın.

deger = 50


def sayi_uj_bej(deger):
    for i in range(1, deger + 1):

        if i % 5 == 0 and i % 3 == 0:
            print(f"ÜjBej : {i}")
        if i % 5 == 0:
            print(f"Bej : {i}")
        if i % 3 == 0:
            print(f"Üj : {i}")


# sayi_uj_bej(deger)

# SORU - 10 :
# Girilen bir cümleyi önce kelimelerine ayıran, sonra da bu kelimedeki harflerin arasına "-" işareti koyan bir fonksiyon yazın.
# Daha sonra kelimeleride "_" karakteri ie birleştirin.
# Cümleyi kelimelere parçalamak için split() fonksiyonunu kullanın.

cumle = "Bu hayat Çok kısa be yigenim"


def cumle_degistir(cumle):
    kelimeler = cumle.split()
    yeni_cumle = ""

    for kelime_index, kelime in enumerate(kelimeler):
        birlesmis_kelime = ""
        for harf_index, harf in enumerate(kelime):
            birlesmis_kelime += harf
            if harf_index < len(kelime) - 1:
                birlesmis_kelime += "-"
        yeni_cumle += birlesmis_kelime

        if kelime_index < len(kelimeler) -1:
            yeni_cumle += "_"
    print(yeni_cumle)



cumle_degistir(cumle)
