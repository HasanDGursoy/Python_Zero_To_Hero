# LISTENİN ARGUMAN OLARAK FONKSİYONA GEÇİLMESİ

# Fonksiyon içinde listeyi değiştirme örneği
harfler = ["a", "b", "c"]
print("Fonksiyona geçilmeden önce ", harfler)


def buyuk_harf_ekle(harf_listesi):
    harf_listesi.insert(1, 'A')
    harf_listesi.insert(3, 'B')
    harf_listesi.insert(5, 'C')


buyuk_harf_ekle(harfler)
print(harfler)

# Listeler, daha doğrusu Non-primitive tipler, bir fonksiyona parametre olarak geçilince :
# kendiler geçer (adresleri geçer) --> Pass By Reference


# Fonksiyon içinde listeye tekrar atama :

def buyuk_harf_ekle(harf_listesi):
    harf_listesi = ["x","y","z"]


buyuk_harf_ekle(harfler)
print(harfler)

# Fonksiyon içinde parametre olarak gelen liste yeniden atanırsa,
# orjinal listeye dokunmamış olur
# fonksiyon içinde yeni bir kopyası oluşmuş olur.

