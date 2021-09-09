# KEY OLARAK LAMBDA FONKSİYONU

# Bazı hazır Python fonksiyonları, işlem yapabilmek için sizden işlemin nasıl yapılacağını anlatan bir fonksiyon isterler.
# Yani parametre olarak bir fonksiyon isterler.
# Daha önce lambda fonksiyonu görmüştük.
# Şimdi lambda fonksiyonu kullanıp çok zor görünen işleri rahatça yapacağız.
# Örneğin, sıralama için kulllanan sort() ve sorted() fonksiyonları.

# sort() şu şekilde çalışır.
# list.sort(reverse = True|False,key=myFunc)
# sorted()
# sorted(iterable,key=myFunc,reverse=True|False)

# işte yukarıdaki iki fonksiyonda key parametresine geçen myFunc fonksiyonu, işleminin nasıl yapılacağını anlatan fonksiyonlardır.
# Önce normal bir fonksiyon yaratıp onu parametre olarak geçelim sonra aynı işlemi lambda ile yaparız.

# örnek : normal fonksiyon ile

arabalar = ('mercedes', 'auidi', 'porsche', 'volswagen')


# bu tuple ı harf uzunluklarına göre küçükden büyüğe sıralayalım.

# önce sıralama fonksiyonu

def myFunc(e):
    return len(e)


# Bu fonksiyonu parametre olarak kullanıcaz DİKKATLİ !!

# sorted() yeni bir liste yaratır.

print(sorted(arabalar, key=myFunc))

# sort() fonksiyonu listeyi yerinde değiştirir.

arabalar_listesi = list(arabalar)
arabalar_listesi.sort(key=myFunc)
print(arabalar_listesi)

# Eğer listeye cast etmeden yazdırsaydık hata alırdık. Çünkü tuple'ın sort özelliği yok :D

################################################################################

# örnek : lambda Fonksiyonu ile yapıcaz.

# Biraz önce myFunc dediğimiz yerde lambda kullanıcaz.

# sorted()

car = sorted(arabalar, key=lambda x: len(x))
print(car)

# sort()

arabalar_listesi = list(arabalar)
arabalar_listesi.sort(key=lambda x: len(x))

print(arabalar_listesi)

# örnek = (2,1,3,7,6,4,5)

sayilar = (2, 1, 3, 7, 6, 4, 5)

# key parametresini biz verelim

sorted(sayilar, key=lambda x: x)  # Bu standart sıralama

# Örnek :

harfler = ['c', 'f', 'b', 'a', 'e', 'd']
harfler.sort(key=lambda x : x) # direk kendisini alacağı için direk standart sıralamaya girer.
print(harfler)