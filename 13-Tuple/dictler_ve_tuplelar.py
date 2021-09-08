# Dict ve Tuple

# items() fonksiyonu bize bir tuple() listesi döner

# ilk 3 harfi ve onların ASCII kodlarını tutan bir sözlük
# ord() fonksiyonu bize ASCII değerini verir.
sozluk = {
    'A': ord('A'),
    'B': ord('B'),
    'C': ord('C'),
    'a': ord('a'),
    'b': ord('b'),
    'c': ord('c')
}

print(sozluk)
print(sozluk.items())

# şimdi dict() üzerine döngü kuralım

for anahtar, deger in sozluk.items():
    print(anahtar, deger)

# Hatırlatma : Her ne kadar yukarıda elemanlar sıralı gelmiş ve sanki Dict'de sıralı duruyor olsa bile index olmadığı için sıra beklemek mantıksızdır.

aylar_gunler = [
    ('ocak', 31),
    ('şubat', 28),
    ('mart', 31),
    ('nisan', 30)

]

print(aylar_gunler)
print(dict(aylar_gunler))
# burdaki olay tuplelardan bir liste oluşturduk ancak dict yapınca bunları öyle güzel çevirdiki dict'e sanki direkt dict yazmışısız gibi.

# Alıştırma

# zip() ve range fonksiyonlarını kullanarak haftanın günlerini bir Dict içinde index'leyelim.

gun_adlari = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
numaralar = range(1, 8)

gunler = zip(numaralar, gun_adlari)

dict_gun = dict(gunler)
print(dict_gun)

# Yukarıdaki işlemi tek satır içinde yapalım
gunlers = dict(zip(numaralar, gun_adlari))
print(gunlers)

# Tuple'ı Dict'e key yapmak

# Daha önce, Dict bölümünde şunu demiştik:
# Tuple'lar Immutable olduğu için, Dict'e key olmak için kullanılabilirler.

adlar = ['Musa', 'Bruce', 'Klark', 'Peter']
soyadlar = ['Arda', 'Wayne', 'Kent', 'Parker']
dereceler = ['AA','DC','FF','FD']

ogrenci_durumu = {}

for ad,soyad,derece in zip(adlar,soyadlar,dereceler):

    ogrenci_durumu[(ad,soyad)] = derece

print(ogrenci_durumu)