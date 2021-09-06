# TERSTEN ARAMA
# Dictionary ile alakalı örneklerimizde hep anahtar kelime ile arama yaptık.
# Şimdi diyelim ki, tersinden yani değer ile arayıp key'i bulmaya çalışalım.
# Normalde, Dictionary'nin yapılma amacı bu değildir.Dolayısıyla ile yapacağımız arama işleminde iki büyük sorun var bizi bekleyen :

# 1.Aynı değeri gösteren birden fazla anahtar olabilir. Bu durumda ya ilkini döneriz yada tümü içeren bir liste dönmemiz lazım.
# 2.Malesef, bu tersten arama işlemi için basit bir yöntem yok. Dolayısıyla serch' ü kendimiz yapmak zorundayız.


def tersten_arama(dict, value):
    # sözlük içinde bulduğumuz ilk değeri geri dönelim

    for key in dict:

        if dict[key] == value:
            # Bu değeri bulduk -- > key
            # bulamassan dönme
            return key
    else:
        # raise hata fırlatır
        raise KeyError('ARADIĞINIZ DEĞERE AİT ANAHATAR BULUNAMADI')


sozluk = {
    'a': 2,
    'b': 1,
    'c': 4,
    'd': 3,
    'e': 2
}
deger = 21

print(tersten_arama(sozluk, deger))

# Diyelim ki , None dönmek yerine hata göstersek. 'ARADIĞINIZ DEĞERE AİT KEY YOK '
