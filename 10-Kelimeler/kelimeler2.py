# ALIŞTIRMA 1 :
# yasak_harf_var_mi adında bir fonksiyon yaratalım
# bu fonksiyon parametre olarak, bir metin ve yasak harfleri içeren bir string alacak.
# eğer metin içerisinde, bu yasak harflerden herhangi biri varsa False hiç biri yoksa true dönecek

file = open('kelimeler.txt')


def yasak_harf_var_mi(metin, yasak_harfler):
    for harf in metin:

        if harf in yasak_harfler:
            return True
    else:
        # for düzgün çalışırsa çalışır.
        return False


cumle = 'Bu bir normal metindir'

yasak = 'ae'  # Burada tuhafıma giden şey ae harflerini ayrı ayrı taradı ve bu çok tuhafıma gitti ben direk ae birleşik olarak içinde varmı diye bakıcak zannettim

fonks = yasak_harf_var_mi(cumle, yasak)
print(fonks)

print("============= ALIŞTIRMA 2 =============================")


# ALIŞTIRMA 2
# Adı ** sadece_sunlari_kullanir ** olan bir fonksiyon tanımlayalım.
# Parametresi , metin ve harflerden oluşan bir string olsun.
# Eğer metin, sadece bu harfleri kullanıyorsa, True kullanmıyorsa False döncek.


def sadece_sunlari_kullanir(metin, harfler):
    for harf in metin:

        # harf gerçekden harf mi, yoksa noktalama işareti mi? -> isalpa()

        if harf.isalpha() and harf not in harfler:
            return False
    else:
        return True


cumle = "ey edip adanada pide ye ZZz"
harfler = "adeinpy"
yazdir = sadece_sunlari_kullanir(cumle, harfler)
print(yazdir)

print("------------------ ALIŞTIRMA 3 --------------------")


# ALIŞTIRMA 3
# 2 numaralı alıştırmadaki fonksiyonu kullanarak :
# lorem kelimelerinden sadece 'ens' harflerini kullanan kelimeleri bulalım.

def lorem_sadece_sunlari_kullanir(harfler):
    for satir in file:

        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]

        if sadece_sunlari_kullanir(kelime, harfler):
            print(kelime)


lorem_sadece_sunlari_kullanir('ens')

print("--------------- ALIŞTIRMA 4 ------------------")


# ALIŞTIRMA 6
# Adı ** hepsini_kullanir ** olan bir fonksiyon yazıcaz.
# Metin ve harfler alıcak
# Eğer metin verilen, harflerin tümünü en az bir kere kullanıyorsa True herhangi bir harfi kullanmıyorsa False.

def hepsini_kullanir(metin, harfler):
    tumunu_kullanir = True

    for harf in harfler:

        # eğer herhangi bir harf metin içinde yoksa  - > False

        if harf not in metin:
            tumunu_kullanir = False

    return tumunu_kullanir


harfler = 'aecbd'
metin = 'araba demir yolundan geçti ve cesim önüne atladı'

deger = hepsini_kullanir(metin, harfler)
print(deger)


# ALIŞTIRMA 7
# 6 numaralı Alıştırma'da tanımladığınız **hepsini_kullanır**  fonksiyonu yazınız.
# Lorem kelimelerinden hangilerinin 'aei' harflerinin hepsinin kullandığını bulalım.

def aei_tespit_edici(harfler):
    file = open('kelimeler.txt')

    for satir in file:

        kelime_ayirici = satir.split()
        kelime = kelime_ayirici[0]

        if hepsini_kullanir(kelime, harfler):
            print(kelime)


aei_tespit_edici('aei')


# ALIŞTIRMA 8 :
# 4. ALIŞTIRMADA **sadece_sunları_kullanir**
# ve 6. ALIŞTIRMADAKİ ** hepsini_kullanir**  fonksiyonlarını beraber kullanarak.

# Lorem kelimelerinden hangilerinin sadece 'fir' harflerini ama bu harflerin tümünü kullandığını bulucaz.

def sadece_tumunu_kullanir(harfler):
    file = open('kelimeler.txt')

    for satir in file:
        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]

        # Şimdi bu kelime sadece harfler ama tüm harflermimi kullanıyor.

        if sadece_sunlari_kullanir(kelime, harfler) and hepsini_kullanir(kelime, harfler):
            print(kelime)


harfler = 'fir'
sadece_tumunu_kullanir(harfler)


# ALIŞTIRMA 9
# Eğer bir kelimenin harfleri alfabetik sırada ise bunu **düzgün kelime** diyelim
# İsmi **duzgun_kelime_mi** olan bir fonksiyon tanımlayalım.
# Eğer kelime, düzgün kelime ise True, değilse False dönsün.

def duzgun_kelime_mi(kelime):
    # python'da alfabetik sıralamı diye bakmak için -> ASCII
    # önce ilk harfi önceki kelime olarak alalım.

    onceki = kelime[0]

    for harf in kelime:

        # bu harf önceki değişkeninin değerinden önce mi geliyor.

        if harf < onceki:

            # eğer harf, öncekiden önce geliyorsa duzgun değildir.
            return False
        onceki = harf
        
    # eğer buraya kadar geldiyse
    return True


print("==========================================")

print(duzgun_kelime_mi('buz'))

# ALIŞTIRMA 10 :
# 9 numaralı Alıştırmadaki **duzgun_kelime_mi **  fonksiyonu kullanarak.
# Lorem kelimelerinden hangilerinin düzgün kelime olduğunu bulalım.

def lorem_duzgun_kelime():

    file = open('kelimeler.txt')

    for satir in file:

        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]

        # şimdi bu kelime düzgün kelime mi ?
        if duzgun_kelime_mi(kelime):
            print(kelime)

lorem_duzgun_kelime()