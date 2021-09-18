"""
Dosya : file, byte dizisidir
"""
"""
Dosya Tipleri: 
1-Binary Tipi
    * pdf,doc
2-Text Tipi
    * txt, xml, html,. py, .java  
"""
"""
Encoding : Verinin byte yapısıdır --> nasıl tutulduğu

İki yaygın encoding şekli : 
1- ASCII (128 karakter)
2- UNICODE (1.114.112) 
"""

# Python'da dosya açmak için --> open()
# Eğer aşşağıda utf-8 encoding ini vermessek ingilizce hariç diller de saçma sapan şeyler ortaya çıkacak.O yüzden ÖNEMLİ
# file = open('kelimeler (1).txt', encoding='utf-8')
# print(file.read())

# Açılmış bir dosya kapanmalıdır. --> close()
# file.close()

# Dosya yoksa --> hata
try:
    file = open('kelimerlsada.txt', encoding='utf-8')
except:
    print('Dosya Bulunamadı')
else:
    print(file.read())
    file.close()

"""
** with ** 
Her seferinde try and cath yapmak yeirne dosya açma,okuma,kapa işlemlerini otomatik yapan yapı
"""

# with open('kelimeler (1).txt',encoding='utf-8') as file:
#    icrerik = file.read()
#    print(icrerik)

# Eğer dosya yoksa --> with FileNotFoundError
try:
    with open('kelimeler (asd1).txt', encoding='utf-8') as file:
        icrerik = file.read()
        print(icrerik)
except:
    print('dosya bulunamadı ...')

"""
Dosya açma şekilleri (Modlar):

* r: okuma (read)
* w: yazma (write)
* a: ekleme (append)
* x: yaratma (create)
* t: text dosyası formatında
* b: binary dosyası formatında
* +: update modu (read + write)
"""

# örnek okuma modu
# r --> okuma
with open('kelimeler (1).txt', mode='rt') as file:
    data = file.read()
    print(data)

# şimdi binary dosyası okuma
with open('5848152fcef1014c0b5e4967.png', mode='rb') as resim:
    data = resim.read()
    print(data)
