# NESNELER VE DEGERLER

a = 'kivi'
b = 'kivi'

print(id(a), id(b))

# Degerlerin id'leri aynı çıktı peki neden farklı değişkenler yaratmamıza rağmen neden id'ler aynı ?
# Python iki değişkenin değeri aynı ve değişkenler Immutable (str) olduğu için
# iki farklı değişken yaratmak yerine ram'den tasarruf edip ikisini aynı adrese yolladı.

b = 'kivis'
print(id(b), id(a))  # b'yi değiştirdik ve artık id de değişti. Python durumu farkedip yeni bir adres yarattı.

# PEKİ YA LİSTE OLSAYDI  ?

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(id(x), id(y))
print(id(x) == id(y))

# '==' kontrolü --> eşitlik (equivalent) ->değer
# id(x) == id(y) kontrolü --> kimlik (identical) -> nesneler
