# PROJE VERİ YAPILARI

# Telif hakkı olmadan yazılı metin kaynağı http://gutenberg.org/
# Kitap olarak Pride and Prejudice by Jane Austen
# ve Alice's Adventures in Wonderland by Lewis Carroll
# Bu projemizde iki farklı kitap üzerinde, python kullanarak çeşitli bilgiler toplayacağız.
# Bu sayede hem şimdiye kadar öğrenmiş olduğumuz kavramları (değişkenler,fonksiyonlar, veri yapıları...) tekrar etmiş olacağız hemde bu kavramları gerçek bir uygulama üzerinde görmüş olacağız.

# Kitapları Okuyalım
# Bu iki kitabı python'a okutarak kitaplarda geçen bütün kelimeleri bulalım.
# Bunu yaparken:
# Noktalama işaretlerini çıkaralım --> string.punctuation
# Boşluk karakterlerini çıkaralım --> string.whitespace
# Kitapların başlangıç ve sonunu bulalım
# Her işlemi kendi fonksiyonunda yapalım
# string modülünü kullanalım

import string
from collections import Counter

# global değişken - 1
# noktalama işaretleri

noktalama_isaretleri = string.punctuation
print(noktalama_isaretleri)

# global degisken - 2
# bolsuk karakterleri

bosluk_karakterleri = string.whitespace
print(bosluk_karakterleri)


# Kitap okuma fonksiyonu yazalım

# dosyadan file getirme fonksiyonu

def file_dondur(kitap_adi):
    kitap_yolu = kitap_adi + '.txt'
    return open(kitap_yolu, encoding='utf-8')


# baslangıç bölümünü atlar
# bu bölüm okuduğumuz kitap'a dahil değildir.

def baslangic_atla(file):
    atlama_metni = '*** START OF THIS PROJECT'

    # file her okumada, okuduğu yere kadar ilerlediği için
    # atlama_metninin değerine kadar okutup çıkarsak okuma yeri artık o ifadenin sonrası olur.

    for satir in file:
        if satir.startswith(atlama_metni):
            break


def sona_gelindi_mi(satir):
    son_metin = '*** END OF THİS PROJECT'

    return satir.startswith(son_metin)


def satirdaki_kelimeler(satir):
    bos_list = []

    kelime_dizisi = satir.split()

    for kelime in kelime_dizisi:

        # eğer kelimede noktalama işaretleri varsa
        kelime = kelime.strip(noktalama_isaretleri)

        # küçük harf yap
        kelime = kelime.lower()

        # alfanumerik mi ?
        if kelime.isalpha() and len(kelime) > 0:
            bos_list.append(kelime)
    return bos_list


def kelimeleri_doldur(file, bos_list):
    # Python dosyayı satır satır okuyacak
    for satir in file:

        # sona gelmişmi '*** END OF THIS PROJECT'

        if not sona_gelindi_mi(satir):
            # satır içindeki kelimeleri alıcaz
            satir_kelimeleri = satirdaki_kelimeler(satir)

            # şimdi kelimeler listemize ekleriz
            bos_list.extend(satir_kelimeleri)


def kitap_oku(kitap_adi):
    """
    Verilen kitap adına göre ilgili kitabı okur.
    :param kitap_adi: string Kitap adı
    :return: list kelimeler
    """
    bos_kelimeler = []

    file = file_dondur(kitap_adi)

    # şimdi '*** START OF THİS PROJECT' KISMINA KADAR ATLAYALIM.
    baslangic_atla(file)

    kelimeleri_doldur(file, bos_kelimeler)

    return bos_kelimeler


# Şimdi pride and prejudice i okuyalım
kitap_adi = 'Pride_and_Prejudice'
pride_kelimeleri = kitap_oku(kitap_adi)
print(pride_kelimeleri[:20])

# Şimdi Alice Adventures in Wonderland i okuyalım

alice_kitabi = 'Alice_Adventures_in_Wonderland'
alice_kelimeleri = kitap_oku(alice_kitabi)
print(alice_kelimeleri[:20])
print()
print('=================================================')
print()


# KELİMELERİ UZUNLUK SIRASINA GÖRE DİZELİM

# Listeleri sıralayan fonksiyon

def liste_sirala(liste, azalan_mi):
    # uzunluk sıralayacaksak --> key parametresini vermemiz lazım lambda
    return sorted(liste, reverse=azalan_mi, key=lambda x: len(x))


# Şimdi pride ... kitabındaki keliemeleri kısadan uzuna sıralyalım.

kelime_sirala_pride = liste_sirala(pride_kelimeleri, False)
print(kelime_sirala_pride[:20])
kelime_sirala_pride = liste_sirala(pride_kelimeleri, True)
print(kelime_sirala_pride[:20])

# Şimdi alice .... kitabındaki kelimeleri kısadan uzuna ve daha sonra uzundan kısaya  sıralayalım
alice_kisa = liste_sirala(alice_kelimeleri, False)
print(alice_kisa[:20])
alice_uzun = liste_sirala(alice_kelimeleri, True)
print(alice_uzun[:20])


# TEKRARLARI SİL

def tekrarlari_sil(liste):
    # tekrarları silmemizin en tatlı yolu --> set()

    kume = set(liste)

    kume = list(kume)

    return kume


pride_kelimeleri_farkli = tekrarlari_sil(pride_kelimeleri)
print(pride_kelimeleri_farkli[:20])


# KİTAPLARDAKİ TOPLAM KELİME SAYISINI BULALIM

def kelime_sayisi(liste):
    return len(liste)


pride_kelime_sayisi = kelime_sayisi(pride_kelimeleri)
print('Pride And Prejudice : ', pride_kelime_sayisi)
pride_tekararsiz = tekrarlari_sil(pride_kelimeleri)
pride_tekararsiz_farkli = kelime_sayisi(pride_tekararsiz)
print('Pride And Prejudice (Tekrarsız) : ', pride_tekararsiz_farkli)


# HANGİ KELİME KAÇ KERE GEÇİYOR

# en yüksek sayıda geçen kelimeyi veren fonksiyon

def sozluk_sirala(dict):
    # önce sözlüğü valuelarına göre sıralıcak
    sirali_liste = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    # bu kısımda neden x[1] yazıyoruz açıklayım
    # dict = {'hasan': 12 } gibi bir sözlük düşün ve bunun valuesu dict[1] tekabul eder bu yüzden yapıyoruz.
    return sirali_liste


def en_yuksek_adetli(liste, n=20):
    # sözlük olarak dönecek
    kelime_adetleri = {
        kelime: liste.count(kelime)
        for kelime in liste
    }
    # bu sözlüğü sıralamamız lazım

    sirali_liste = sozluk_sirala(kelime_adetleri)

    # şimdi en yüksek n adet alalım
    sirali_liste_top = sirali_liste[:n]
    return dict(sirali_liste_top)

# Not : sakın pride_kelimeleri ile çalıştırmayın 1 gün flan sürer üzer bu durum be :D

alice_kelime_adetleri_fn = en_yuksek_adetli(alice_kelimeleri)
#print(alice_kelime_adetleri_fn)


# Ancak bu fonksiyonu bu şekilde yazmak doğru değil bunun yerine Counter kullanalım.

# COUNTER
# Counter liste ne kaç kere geçiyorsa bize frekansını söyler
pride_kelime_adetleri = Counter(pride_kelimeleri).most_common(20) #en yüksek 20 adetli aldık.
sozluk_pride = dict(pride_kelime_adetleri)
print(sozluk_pride)
