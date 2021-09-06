import keyword
# Degiskenler python da genelde snake_case yazılır.
# Degiskenler sayıyla başlayamaz, önceden tanımlı fonksiyon isimlerle , boşlukla ve özel karakterlerle kullanılamaz.

 # PYTHON VERİ TİPLERİ

"""
Text Tipi = str
Numerik Tipler = int,float
Liste Tipleri = list, tuple, range
İliski Tipi = dict
Küme Tipi = set
Booelean Tipi = bool

type öğrenmek için print(type(x))
"""

# PYTHON GENEL YAPISI

"""
Derleyici (Compiler) = Kaynak kodu, makine diline tek seferde çevirir. örn = C, C++

Yorumlayıcı(Interpreter) = Kaynak kodu, makine diline kodları yazarken çevirmeye başlar. örn = Python,Ruby,Java

Python interpreter , yorum satırlarını göz ardı eder ve yazdırmaz sadece yazılımcı görür.


"""

# String ifadelerde alta satıra inmek için imkan vardır bunu \n işareti ile yaparız.
print("1.Satır\n2.Satır\n3.satır")

# PYTHON'DA NUMERİK OPERASYONLAR

a = 30
b = 20
print(a*b)
print(b/a*a)
# Toplama vs hepsi sembol ardından eşittir işareti koyularak ypılabiliyor örn= a = a +1 yazmak yerine a+=1
a += 3
b +=1
print(a,b)
#Bölme
a /=10
print(a)
#Çarpma
b*=a
print(b)

# String ifadeler hem tek tırnak hemde çift tırnak ile yazdırılabilir.

poem1 = "Be or not be"
poem2= 'Die mf die close your eyes'
print(poem1)
print(poem2)

# ANAHTAR KELİMELER

anahtar_kelimeler = keyword.kwlist
print(anahtar_kelimeler)

# Peki herhangi bir kelime python için keyword mü nasıl anlicaz ?

# Bunun için yine keyword paketinin methodunu kullanıcaz.
print(keyword.iskeyword('not'))
print(keyword.iskeyword('word'))