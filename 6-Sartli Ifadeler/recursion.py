"""
RECURSİON - kendi kendini çağırmak

# Bir fonksiyon başka fonksiyonları çağırabildiği gibi, kendisinide çağırabilir.
# Buna RECURSİON  adı verilir.
# Örneğin verilen bir sayıdan geriye doğru, 0'a kadar sayan bir fonksiyon

# ÖNEMLİ NOT : RECURSİON'larda durma koşulu çok önemlidir. Eğer  fonksiyon nerde duracağını bilmesse, sonsuz döngüye girer.
"""
# RECURSİON methodlar ilk başta mantık kurması zor methodlardır. Deli gibi ram yer kullanılması çok tavsiye edilmez ama bazı problemler sadece recursion methodlar ile çözülür.

def geri_say(n):
    if n <= 0:
        print("----- Program Sonu -----")
    else:
        print(n)
        geri_say(n-1)

geri_say(5)

def metni_yaz(metin,n):

    # önce durma koşulu

    if n <= 0:
        return
    else:
        print(metin+" : {0} ".format(n))
        metni_yaz(metin,n-1)

metni_yaz("Machine Learning",5)

