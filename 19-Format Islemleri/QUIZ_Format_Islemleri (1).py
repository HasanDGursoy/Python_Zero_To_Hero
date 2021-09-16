"""
 Format İşlemleri ile ilgili QUIZ - 10 Soru
"""

# --------------------------------------------------------------------------------------#

# Soru 1:
from string import Template

"""
Adı gun_adi olan bir fonksiyon yazın.
Fonksiyon kullanıcıdan bir gün istesin ve bu günün adını ve harf sayısını Tuple olarak dönsün:
Ör: ('Pazartesi, 9)

Bu fonksiyondan veriyi alıp, % operatorünü kullanarak şu şekilde ekrana yazdırın:
'Pazartesi gününün harf sayısı: 9'
"""


# Çözüm 1:

def gun_adi():
    inp = input('Lütfen bir gün adı verin : ')
    sablon = '%s  günü harf sayısı : %d' % (inp, len(inp))
    print(sablon)


# gun_adi()
# --------------------------------------------------------------------------------------#

# Soru 2:
"""
Soru 1'deki gun_adi fonksiyonunu çağırın ve sonucu str.format() fonksiyonunu kullanarak şu şekilde yazdırın:
Ör: 'gün: Pazar, uzunluk: 5' 
"""


# Çözüm 2:

def gun_adi():
    inp = input('Gün adı giriniz : ')
    sablon = 'gün : {0}, uzunluk : {1}'.format(inp, len(inp))
    print(sablon)


# gun_adi()

# --------------------------------------------------------------------------------------#

# Soru3:
"""
Soru 1'deki gun_adi fonksiyonunu çağırın ve sonucu f-strings kullanarak şu şekilde yazdırın:
Ör: 'gün: Pazar, uzunluk: 5'
"""


# Çözüm 3:

def gun_adi():
    inp = input('Gün adı giriniz : ')
    sablon = f'gün : {inp} , uzunluk : {len(inp)}'
    print(sablon)


# gun_adi()


# --------------------------------------------------------------------------------------#

# Soru 4:
"""
Soru 1'deki gun_adi fonksiyonunu çağırın ve sonucu Template Strings ile şu şekilde yazdırın:
Ör: 'gün: Pazar, uzunluk: 5'
"""


# Çözüm 4:

def gun_adi():
    inp = input('Lütfen gün adı giriniz : ')
    sablon = Template('gün : $gun , uzunluk : $uzunluk').substitute(gun=inp, uzunluk=len(inp))
    print(sablon)


# gun_adi()


# --------------------------------------------------------------------------------------#

# Soru 5, 6, 7, 8, 9, 10 için aşağıdaki sözlüğü (dict) kullanınız:
baskent = {
    'Türkiye': 'Ankara',
    'Almanya': 'Berlin',
    'İngiltere': 'Londra',
    'ABD': 'Washington'
}

# --------------------------------------------------------------------------------------#

# Soru 5:
"""
baskent sözlüğünü ve % operatorünü kullanarak ekrana şu şekilde yazdırın:
"Türkiye'nin başkenti Ankara'dır"
Türkiye kelimesi sabit, Ankara değişken olacak.
"""
# Çözüm 5:

print('Türkiyenin başkenti %(Türkiye)s dır' % baskent)
# --------------------------------------------------------------------------------------#

# Soru 6:
"""
baskent sözlüğünü ve str.format() fonksiyonunu kullanarak ekrana şu şekilde yazdırın:
"Almanya'nın başkenti Berlin'dir"
Almanya ve Berlin kelimelerinin ikisi de değişken olacak.
"""
# Çözüm 6:

print('Almanyanın başkenti {0} dir'.format(baskent['Almanya']))
# --------------------------------------------------------------------------------------#

# Soru 7:
"""
baskent sözlüğünü ve f-strings kullanarak ekrana şu şekilde yazdırın:
"İngiltere'nin başkenti Londra'dır"
İngiltere ve Londra kelimelerinin ikisi de değişken olacak.
"""
# Çözüm 7:

print(f'İngilterenin başkenti {baskent["İngiltere"]} dir')

# --------------------------------------------------------------------------------------#

# Soru 8:
"""
baskent sözlüğünü ve Template Strings kullanarak ekrana şu şekilde yazdırın:
"ABD'nin başkenti Washington'dır"
ABD ve Washington kelimelerinin ikisi de değişken olacak.
"""
# Çözüm 8:

print(Template('ABDnin başkenti $k dir').substitute(k=baskent['ABD']))

# --------------------------------------------------------------------------------------#

# Soru 9:
"""
for döngüsü ve f-strings kullanarak baskent sözlüğü içindeki ülke-başkent ikililerini
şu şekilde ekrana yazdırın:
<başkent>, <ülke>nin başkentidir.

Ör: Ankara, Türkiye'nin başkentidir.
"""
# Çözüm 9:
print()
for key, val in baskent.items():
    print(f'{key} nin başkenti {val}')


# --------------------------------------------------------------------------------------#

# Soru 10:
"""
comprehension ve f-strings kullanarak baskent sözlüğü içindeki ülke-başkent ikililerini
şu şekilde ekrana yazdırın:
<başkent>, <ülke>nin başkentidir.

Ör: Ankara, Türkiye'nin başkentidir.
"""
# Çözüm 10:

[print(f'{val} , {key} nin başkentidir.')
    for key,val in baskent.items()
]
# --------------------------------------------------------------------------------------#
