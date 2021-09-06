# Dictionary
# Dictionary sözlük demekdir.
# List'in daha genel yapısı olarak düşünebiliriz.
# Dictionary'de indexleri biz belirleriz ve sadece tam sayı değil hemen hemen her tür olabilir.
# yapısı:
# { key : value} şeklindedir.

ingTR = {}
type(ingTR)

# araba

araba = {
    "Auidi": "Almanya",
    "Mazda": "Japonya",
    "Fiat": "İtalya"
}
print(araba)
print(type(araba))

# dict() ile yaratma

trING = dict()
print(type(trING))

araba2 = dict({
    'auidi': 'almanya',
    'mazda': 'japonya',
    'fiat': 'italya'
})
print(araba2)

# Önemli Not

# Listelerde index ile erişilir ->list[0]
# Dictionaryde index alma yok.
# [] içine index numrası değil --> key yazılır.


print(araba2['auidi'])  # elemanlara bu şekilde ulaşabiliriz.

# Dictionary Eleman Ekleme

# Listelerde eleman eklemek için --> append(),insert()
# Dictionary için bu methodlar yoktur.

ingTR = dict()

ingTR['one'] = 'bir'
ingTR['ignore'] = 'görmezden gelmek'
ingTR['mouse'] = 'fare'
print(ingTR)

# degeri yanlış yazalım
ingTR['six'] = 'altti'

# Bunu düzeltmek için değere tekrar atama yapıcaz.
ingTR['siz'] = 'alti'

# update() methodu

arac = {
    'marka': 'ford',
    'model': 'mustang',
    'yil': 1964
}

# arac sözlüğüne renk ekleyelim

eklenecek = {'renk': 'kırmızı'}
arac.update(eklenecek)

# tek seferde birden fazla özellik eklemek istesydik.

eklenecekler = {'fiyat': 300000,
                'km': 89000,
                'motor': 1.6
                }
arac.update(eklenecekler)
print(arac)

# Eleman silmeye de bakalım

# Listlerde eleman silmek için = pop(), del ve remove() kullanılıyordu
# Güzel haber pop ve del dict için de kullanılabiliyor..
print("=============================== Silme işlemi =======================")
# pop()

print(ingTR)
ingTR.pop('mouse')
print(ingTR)

del ingTR['siz']
del ingTR['six']
print(ingTR)
