# LİSTEDEN ELEMAN SİLMEK (DELETE)

# 1- Eğer silinecek elemanın index'ini biliyorsak -> pop(index)

dizi = ["x", "y", "z", "t"]

# pop fonksiyonu bize silinen elemanı geri döner.

silinen = dizi.pop(2)
print(dizi)
print(silinen)

# Eğer pop()' a index vermessek en sondaki elemanı siler

dizi.pop()
print(dizi)

# 2 - Eğer silinen elemana ihtiyacınız yoksa : del
dizi = ["k", "l", "m", "n", "o"]

# dizinin 2. indexteki yani 'm' yi silelim.

del dizi[2]
print(dizi)
del dizi[3]
print(dizi)

# TEK SEFERDE BİRDEN FAZLA ELEMANI SİLMEK İÇİN --> SLİCE YAPIP SİLİCEZ

t = ["a", "b", "c", "d", "e", "f"]

# 1. indexden 5. indexe kadar silelim

del t[1:5]
print(t)

# EĞER SİLİNECEK ELEMANIN KENDSİNİ BİLİYORSAK (İNDEX DEĞİL) -->> REMOVE()

guzel_dizi = ["a","b","c","d","e","f"]

guzel_dizi.remove('f')