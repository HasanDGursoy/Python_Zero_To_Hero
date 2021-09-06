# Dictionaray'nin Elemanları Üzerinde Dönme

arabalar = {
    'auidi': 'almanya',
    'mazda': 'japonya',
    'fiat': 'italya',
    'ford': 'amerika'
}

# items(),keys(),values()

for araba in arabalar.items():
    print(araba)

# destructuring
for marka, ulke in arabalar.items():
    print(marka, ' : ', ulke)

for k in arabalar.keys():
    print(k)

for v in arabalar.values():
    print(v)

print()
print("====================== ALIŞTIRMA =============================")
print()


# Alıştırma :

# Fonksiyon yaratalım. Metnin harflerini saysın, kaç kere geçtiğini bir sözlükde dönsün

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


metin = 'Bu metinde hangi harf kaç sefer geçer ? '
harf_sozlugu = harf_say(metin)
print(harf_sozlugu)


# Çözüm 2
# Pythonic
# Get() ile çözücez çünkü
# marka.get('x',0) yazarsak  = markanın içinde x yoksa 0 döndür demektir.

def harf_say2(metin):
    harfler = dict()

    for harf in metin:

        if harf.isalpha():
            harfler[harf] = harfler.get(harf, 0) + 1
            # yukarıdaki olayın logic'i şudur :
            # içinde varsa kendini döndür 1 ekle
            # içinde yoksa 0 döndür 1 ekle

    return harfler


metin_dondur = harf_say2(metin)
print(metin_dondur)
