"""
Eski stil formatlama (%)

- %s -> string olarak formatlar
- %d -> integer
- %f -> float
    -%f.<karakter sayısı 0 dan sonra>f
"""

import math

gun = 'Pazartesi'
print('Bu gun günlerden %s' % gun)

sayi = 20
print('Euclide göre %d bir mükemmel sayıdır.' % sayi)

pi = math.pi
metin = "pi sayisi : %.4f" % pi
print(metin)

# birden fazla % operatoru

bilgi = "Python, ilk olarak %d de yayınlandı ve %.2f yıldan fazladır kullanılıyor." % (1991, 30)
print(bilgi)

# Tuple olarak % operatoru kullanılır.

veri = ("Peter", "Parker", 28)
soru = 'Selam %s %s . Senin yaşın %d, değilmi ?'
print(soru % veri)

# Dictionary ile

dosya = {
    'path': './com/pyt',
    'version': 1.8,
    'author': 'joker'
}
bilgi = 'adresi %(path)s olan , %(version).1f versionlu dosyayı %(author)s yazmıştır' % dosya
print(bilgi)
