# LIST AND STRINGS
# String bir karakter dizisi,List ise değerler dizisidir.
# İkiside dizidir.
# Eğer bir String'i, List'e çevirmek istersek list() yapıcısını (constructor) kullanılır

gun = 'pazartesi'
print(gun)
print(type(gun))

gun_harfleri = list(gun)
print(gun_harfleri)
print(type(gun_harfleri))

# Eğer değişkenin ismi list ise list methodunu kullanamayız.
# örnek list = [1,2,3] dedik ve daha sonra methodu kullanmaya çalıştık
# gun = list[gunler] burdaki list methodu çalışmayacak çünkü değişkeni algılayacak. :S
# Python'un hazır veri tiplerini bir değişken adı olarak kullanmayın ÖNEMLİ !!

metin = "bu gün hava biraz soğuk"
print(metin)
kelimeler = metin.split()
print(kelimeler)
print(type(kelimeler))

# Metnin harflerini bir listeye almak isteseydik
harfler = list(metin)
print(harfler)

mail_box = 'spam-spam-spam-spam'
karakter = '-'
mailler = mail_box.split(karakter)
print(mailler)

# Join() fonksiyonu split() fonksiyonun tam tersidir

kelimelers = ["Güneş", "Açar", "Yüzler", "Güler"]

cumle = ' '.join(kelimelers)  # Başına boşluk koyarak birleştir demektir.
print(cumle)
cumle = '-'.join(kelimelers)
print(cumle)

