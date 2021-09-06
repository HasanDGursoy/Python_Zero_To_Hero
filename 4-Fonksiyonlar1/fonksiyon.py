import math

# Fonksiyonlar kod tekrarını önler. Parametre alır yada almaz duruma bağlı.

print(int(5.123))
print(str(123.123123))

# MATEMATİK FONKSİYONLARI
# "math" modülü kullanıcaz . Modül = Bir biri ile ilgili fonksiyonları ve dosyları bir arada tutan dosya kümeleridir.
# Python da help fonksiyonunu kullanarak modüllerin ne işe yaradığını öğrenebiliriz.

# help(math)

# Yarı çapı 10 cm olan bir çevresi ne kadardır ?

r = 10

# Cevre

cevre = 2 * math.pi * r
print(cevre)

# 30 derecenin sinüsü

derece = 30

# Radyan
radyan = math.radians(derece)
print(radyan)

help(math.sin)

sinus = math.sin(radyan)
print(sinus)

# Fonksiyonların birleşimi olarak bunu yapmak

sinus = math.sin(math.radians(derece))
print(sinus)  # bu şekilde yazarsak daha güzel olur.


# FONSKİYON TANIMLAMA (FUNCTION DEFINITION)

def fonksiyon_adi(name):
    return name


name = fonksiyon_adi("hasan")
print(name)


# Pythonda indent yapısı ile kod bölümlendirilir.
# tab tuşu yada 4 space tuşu

# Parametresiz Fonksiyon tanımla

def ogrenci_adi_yasi_dili():
    print("Adı : John Doe")
    print("Yaş : 22")
    print("Dil : Python")
    name = fonksiyon_adi("hasan")
    print(name)


ogrenci_adi_yasi_dili()

# İŞLEME SIRASI (EXECUTION FLOW):
# Kodlar yukarıdan aşşağıya çalışmaya başlar.


# PARAMETRELİ FONKSİYONLAR

def diktorgenCevre (uzun_kenar,kisa_kenar):

    diktorgen_cevre = (uzun_kenar+kisa_kenar) *2

    print(diktorgen_cevre)

diktorgenCevre(10,20)

def ad(name):
    print("Adı : "+name)

def soy_ad(surname):
    print("Soy Adı : "+surname)
def yas (old):
    print("Yaş : "+str(old))
def dil(language):
    print("Dil : "+language)

def herseyi_yazdir(name,surname,old,language):
    ad(name)
    soy_ad(surname)
    yas(old)
    dil(language)

herseyi_yazdir("hasan","gürsoy",50,"Türkçe")