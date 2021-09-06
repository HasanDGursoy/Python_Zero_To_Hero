# LİST LER DİCT LERDE DEĞER OLARAK ATANABİLİR.

def harf_say(metin):
    harfler = dict()

    for harf in metin:

        # harf istediğimiz için --> isalpha()

        if harf.isalpha():

            # harf'i harfler sözlüğüne ekle --> içinde var mı ?
            # varsa değeri 1 arttır.
            if harf in harfler.keys():
                harfler[harf] += 1
            else:
                # yoksa , ilk defa geliyordur -> değeri ile eklenecek
                harfler[harf] = 1

    return harfler


# Bir örnek yapalım anlaşılsın

def harf_listele(metin):
    # önce metin verip sözlük alalım

    sozluk = harf_say(metin)

    # boş sözlük yaratalım

    harfler = dict()

    for key in sozluk:

        # değerini alalım
        deger = sozluk[key]

        # bu değer daha önceden harflere eklenmişmi ?
        # in ifadesi ile kontrol et

        if deger not in harfler:

            # yoksa ekle --> liste olarak eklicez bu sefer : []
            harfler[deger] = [key]

        else:
            harfler[deger].append(key)

    return harfler


metin = 'Bu metinde hangi harf kaç kere vardır ? '
harfler = harf_listele(metin)
print(harfler)

# ÖNEMLİ NOT
# Listler, Dictionary'lerde value olarak kullanılabilir.
# Ama key olarak kullanılamazlar.

a = [1, 2]
s = dict()

s[a] = 'hooop'

# Kod patladı :D demekki dict'de key bir list olamaz.

# Son Söz

# 1. Key'ler tekil yani unique olmalı.Aynı key kullanılamaz.
# 2. Key'ler Immutable yani Değiştirilemez.Hashtable yapısından ötürü.
# 3. Key olabilecek tipler : int,float,bool,str,tuple,frozenset
