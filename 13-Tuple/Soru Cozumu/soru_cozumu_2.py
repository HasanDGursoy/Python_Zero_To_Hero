# Soru - 6
# Parametre olarak bir liste alan bir fonksiyon yazın. Fonksiyonun adı, tuple_sonunu_degistir olsun.
# Bu listenin elemanları birer tuple olsun.
# Her ibr tuple farklı uzunlukta olabilir.Dolayısı ile istenin elemanlarının uzunlukları sabit değil.
# Yazacağınız fonksiyon, liste içindeki herbir tuple elemanının son üyesini silsin, yerine karesini yazsın.

# İpuçları
# Liste yerinde değişssin, yani parametre olarak gelen orjinal liste değişssin.
# Tuple'ın son elemanınını index ile nasıl alacağınızı düşünün.
# Listenin içinde for ile dönerken döngüdeki elemanı değiştirirseniz de liste değişmez.
# Listeyi değiştirmenin bir yolunu bulmalısınız.(enumarete())
# tuple birleştirmeye dikkat ediniz (tek elemanlı bir tuple nasıl olur.)

def tuple_sonu_degistir(liste):
    for i, val in enumerate(liste):
        # önce tuple'in son elemanına kadar al
        son_elemana_kadar = val[:-1]

        # son eleman için -> kare al
        son_eleman = val[-1] ** 2

        # şimdi bu ikisini birleştir

        val = son_elemana_kadar + (son_eleman,)

        liste[i] = val


tuple_listesi = [(2, 5, 8), (4, 3), (1, 7, 9, 6), (5,)]
print(tuple_listesi[0][-1])  # Bu benim taktik.

print("*******************************************")
tuple_sonu_degistir(tuple_listesi)


# SORU - 7
# Parametre olarak bir liste alan bir fonksiyon yazın.Fonksiyonun adı, tuple_karesi_ile_degistir olsun.
# Bu listenin elemanları birer tuple olsun
# Her bir tuple farklı uzunlukda olabilir.Dolayısı ile listenin elemanlarının uzunlukları sabit değil.
# Yazacağınız fonksiyon liste içindeki her bir tuple elemanının tüm elemanlarının yerine karelerini yazsın.
# ve yeni kareli listeyi geri dönsün

# İpuçları
# Parametre olarak gelen orjinal liste değişmesin
# Listenin içinde for ile dönerken, döngüdeki elemanı değiştirsenizde liste değişmez.

def tuple_karesi_ile_degistir(liste):
    yeni_liste = liste.copy()

    for index, tup in enumerate(yeni_liste):

        yeni_tup = tuple()

        # tup'un elamnları üzerinde gez.

        for t in tup:
            yeni_tup += (t ** 2),

        yeni_liste[index] = yeni_tup


tuple_listesi = [(2, 5, 8), (4, 3), (1, 7, 9, 6), (5,)]

deger = tuple_karesi_ile_degistir(tuple_listesi)
print(deger)


# SORU - 8
# Direk çözüm soru cok uzun yazmaya üşendim.

def oyuncu_film_karakteri_yil(oyuncular, karakterler, filmler, yillar):
    sozluk = {}

    for oyuncu, karakter, film, yil in zip(oyuncular, karakterler, filmler, yillar):
        # ikili olarak tuple haline getirelim.
        sozluk[(oyuncu, karakter)] = (film, yil)

    return sozluk


oyuncular = ['Marlon Brando', 'Heath Leadger', 'Natalie Portman', 'Emma Stone']
karakterler = ['Don Vito Corleone', 'Joker', 'The Swan Quen', 'Mia']
filmler = ['The Godfather', 'The Dark Knight', 'Black Swan', 'La La Land']
yillar = [1972, 2008, 2010, 2016]

sozluk_oyuncu_film = oyuncu_film_karakteri_yil(oyuncular, karakterler, filmler, yillar)
print(sozluk_oyuncu_film)


# SORU - 9
# Parametre olarak bir Tuple alan bir fonksiyon yazın.Adı tuple_sirala olsun.
# Parametre olarak gelen tuple içinde Tuple'lar tutan bir yapı olsun.Yani elemanlar da tuple olsun. Ve bu elemanlardan herbiri 2 elemanlı bir tuple olacak.
# Fonksiyon parametre olarak gelen tuple'ı sıralayacak ve sıralı bir tuple dönecek.
# Sıralama kuralı , 2.eleman olacak yani içerideki Tupleların 2.elemanına bakıp ona göre sıralayacak.
# ipuçları  = lambda

def tuple_sirala(t_listesi):

    return sorted(t_listesi,key=lambda x : x[1])


# SORU - 10
# Parametre olarak sayılardan oluşan bir tuple ve bir sayı alan bir fonksiyon yazın. Adı kac_kere_var olsun.
# Fonksiyon, Tuple içinde verilen sayının kaç kere geçtiğini versin.
# Bunu yaparken Soru 4'teki kac_kere_geciyor fonksiyonunu kullansın. Kendi bir hesaplama yapmasın yani.
# Eğer bu tupple içinde sayı yoksa , sayı bulunamadı diye hata dönsün.
# İpuçları
# fonksiyon dönen fonksiyon
# raise
# index()

def kac_kere_geciyor(tup, index):
    deger = tup[index]

    return tup.count(deger)

def kac_kere_var(tup,sayi):

    # Tuple içinde sayı varmı ?

    if not sayi in tup:
        raise Exception('Sayi Bulunamadı !')

    else:

        # tuple.index() -> bulduğu ilk indexi döner
        index = tup.index(sayi)

        # fonksiyonu cagır
        return kac_kere_geciyor(tup,index)
