deger = 250


def scope():
    scope_degiskeni = 100
    print(deger)  # bunu yazdırabiliriz çünkü global olarak tanımlı
    print(scope_degiskeni)


scope()

# scope fonksiyonun içindeki scope_degiskeni ne dışarıdan ulaşmaya çalışırsak hata alırız.
# print(scope_degiskeni) dersek hata alırız çünkü onun geçerli oldugu alan sadece scope fonksiyonunda.
# ama global scopeda tanımlanmış bir değişkene fonksiyon içinden ulaşabiliriz.


# GLOBAL SCOPE OLUŞTURMA
name = "hasan"


def isim_yazdir():
    global name
    name = "casim"
    print(name)


isim_yazdir()
print(name)  # fonksiyon içinde global oldugunu söyleyip tekrar tanımladıgımız için "hasan ismi casim ismi ile değişti"
