"""
# FONKSİYONLAR 1.SINIF VATANDAŞDIR.

* Atanabilirler.
* Parametre olarak geçilebilirler.
* Yeniden değer atanabilir.
"""

def kup(x):
    return x**3

print(kup(1205))

# Yukarıdaki fonksiyonu değişkene aticaz ama parantez yok

a = kup # Bu duruma alising = "Yeniden Adlandırma" deniyor.
print(a(15))
print(type(a))

def selamla(metin):
    print("Selamlar, ",metin )

merhaba = selamla
merhaba("hasan")

# PARAMETRE SAYISI ÖNCEDEN BİLİNMİYORSA "*args"
# jenerik toplama fonksiyonu

def toplam(*args):
    return sum(args)
topla =toplam(20,30,50,200,500)
print(topla)

def yazdir(*args):

    for i in args:
        print(i)
        print("-------------")
yazdir(15,"hasan",True,False,20.3)


























