# DEĞİŞTİRİLEBİLİR X DEĞİŞTİRİLEMEZ (Mutable vs. Immutable)
# Python da herşey bir nesnedir.Ve her nesnenin bir tipi vardır.
# Immutable : Bazı tipler atandıkları gibi kalırlar.Yani bir parçası (içinden bir parçaya) değiştirilemez.
# Mutable : Bazı tiplerin ise parçasını değiştirebiliriz.

"""
* int : integer -> Immutable
* float : float -> Immutable
* bool : Boolean -> Immutable
* str : String -> Immutable
* list : List -> Mutable
* tuple : Tuple -> Mutable
* dict : Dictionary -> Mutable
* set : Set -> Mutable
"""
# Yeniden atamak mute etmek değildir.

metin = "Jacki Chan"
# bu ifadeyi değiştirmek istiyorsak yeniden aticaz
metin = "Selam"
print(metin)

# PASS BY VALUE & PASS BY REFERANCE

dil = "Python"
print("Fonksiyona parametre gelmeden önce : ",dil)

def degistir(ad):
    ad = "java"
    print("java")
degistir(dil)

print("Fonksiyona parametre geldikden sonra : ", dil) # Bakın değişmedi çünkü str immutable'dır.
print("=================================================================")

sayilar = [1,2,3,4,5]
print("Fonksiyona parametre olarak geçmeden önce : ",sayilar)

def degistir(dizi):
    dizi[0] = "a"
    dizi[1] = "b"
degistir(sayilar)
print("Fonksiyona Parametre olarak geçtikden sonra : ",sayilar)

# Bu sefer değişti çünkü listeler mutable yani değişebiliyor.