# PROJE - KELİMELER

"""
Bu uygulamada, belli kriterlere göre kelime arama yapacağız.
Örneğin, içinde hiç sesli harf bulunmayan kelimeler hangileri yada harfleri alfabetik sıralanmış kelimeler hangileridir gibi.
Kelimeler bize lorem ipsum olarak gelecek.

"""

# Hazırlık
# Kelimeleri okumak için

"""
* open() fonksiyonu
    * open(file,mode)
    *mods:
        * r : read ()
        * a : append
        * w : write
        * x : create
"""

# open() fonksiyonu ile bir dosya açalım -> file nesnesi verir.

file = open('kelimeler.txt')

# ilk satırını okuyalım
print(file.readline())
print(file.readline())

# Buradaki özel karakterler nelerdir.
# * \n : yeni satır (new line)
# * \r : enter tuşu (carriage return)

satir = file.readline()
print(satir)

# split() fonksiyonu, default olarak boşluk karakteri ailesinden ayırma yapar (space, \n, \r, \t)
# geriye bir dizi döndürür.

print(satir.split())

# Şimdi gereken parçaları öğrendiğimize göre, ilk 20 kelimeyi okuyalım.

# Baştan okumaya başlamak için tekrar baştan yazmak gerekiyor.

file = open('kelimeler.txt')
# readline işlemini for döngüsü bizim için yapıyor.

for index, line in enumerate(file):

    if index <= 20:
        kelime_dizi = line.split()
        print(kelime_dizi)
    else:
        break

print(" ALIŞTIRMA 1 ----------------------------------------")
file = open('kelimeler.txt')
# Alıştırma 1 :

for satir in file:

    # satiri kelime dizisine dönüştürelim
    kelime_dizi = satir.split()

    # şimdi kelime_dizisi (tek elemanlı bir list) içindeki kelimeyi alalım.
    kelime = kelime_dizi[0]

    # 10 karakter kontrolü

    if len(kelime) > 10:
        print(kelime)
print(" ALIŞTIRMA 2 -----------------------------------------------")
# Alıştırma 2
# Şimdi yeni bir fonksiyon yazalım.
# Bu fonksiyon içinde sesli harf bulunmayan tüm kelimeleri bize versin.
# dosyayı tekrar okuyalım

file = open('kelimeler.txt')

for satir in file:

    # İngilizce sesli harfler : a,e,i,o,u
    # satir'i kelime dizisine dönüştür.
    kelime_dizi = satir.split()

    # şimdi kelimeyi alalım
    kelime = kelime_dizi[0]

    # tüm seslileri tek tek kontrol etcez.
    if not 'a' in kelime and \
            not 'e' in kelime and \
            not 'i' in kelime and \
            not 'o' in kelime and \
            not 'u' in kelime:

        print(kelime)

print(" ALIŞTIRMA 3 ======================================================")
# Şimdi içinde 'ae' harflerinin beraber geçtiği kelimeleri bulalım.
file  = open('kelimeler.txt')

for satir in file:

     kelime_dizi = satir.split()
     kelime = kelime_dizi[0]

     if 'ae' in kelime:
         print(kelime)





















