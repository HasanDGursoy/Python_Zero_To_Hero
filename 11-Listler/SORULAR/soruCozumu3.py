# SORU - 8
# Sırala fonksiyonu oluşturup liste ile beraber tipi boolean olan azalan_mi adında bir parametre alsın.Bu parametrenin default değeri False olsun
# Eğer azalan_mi parametresi True ise fonksiyon listeyi büyükden küçüğe sıralasın.
# Eğer azalan_mi parametresi Fals ise listeyi küçükden büyüğe sıralasın.

# sonunda sıralanmış listeyi dönecek.

def sirala(liste, azalan_mi=False):
    sirali_liste = []

    if azalan_mi:
        sirali_liste = sorted(liste, reverse=True)
    else:
        sirali_liste = sorted(liste)

    return sirali_liste


# Şimdi daha ustaca birşey göstericem tek satırda çözücez.

def sirala2(liste, azalan_mi=False):
    return sorted(liste, reverse=azalan_mi)


# gördünümüz ne kadar basit :D

# SORU - 9
# Matematikde  ardışık sayılar bir listedir.
# Gauss Yöntemi ardışık sayıların toplamını veren bir yöntemdir. Ve şu şekilde çalışır
# Önce listeyi küçükden büyüğe yazar.
# Sonra listeyi büyükden küçüğe yazar.
# Bu iki listeyi index bazlı alt alta toplar.
# Bulduğu değeri 2 ye böler çünkü listeyi 2 kere yazmıştır.

# Bu soruda 20' den başlayıp 300'e kadar 5'er 5'er artarak giden sayıların toplamını Gauss Yöntemi ile bulan bir fonksiyon yazalım.
# parametrelerin adları ve default değerleri şu şekilde olsun.
# baslangic --> 1
# bitis --> 100
# artis --> 2

def gauss(baslangic=1, bitis=100, artis=2):
    # önce list oluştur

    liste = list(range(baslangic, bitis, artis))

    # listenin tersi
    ters_liste = liste[::-1]

    # toplam
    toplam = 0

    for i in range(len(liste)):
        ikili_toplam = liste[i] + ters_liste[i]
        toplam += ikili_toplam

    sonuc = toplam / 2

    return sonuc


ardisik_toplam = gauss(10, 50, 1)
print(ardisik_toplam)


# Bu soruyu çözmenin ikinci yolu var.
# True gaussion way

def gauss_2(baslangic=1, bitis=100, artis=2):
    # önce list oluştur.
    liste = list(range(baslangic, bitis, artis))

    toplam = 0

    for i in range(len(liste)):
        ikili_topam = liste[i] + liste[-i - 1]
        # liste[-i-1] gauss yönteminde iki listenin toplamı 11 çıkması lazım her index toplamı için bunu sağlamak için böyle bir yol deniyoruz.
        toplam += ikili_topam

    return toplam / 2
