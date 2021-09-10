# SORU - 1
# Önce for döngüsü ile 1' den 10'a kadar sayıların karelerini veren bir fonksiyon yazın.
# Arından aynı fonksiyonu comp ile yazın .

# önce klasik
bos_liste = []
for i in range(1, 10):
    bos_liste.append(i ** 2)
print(bos_liste)

# comp ile yapalım

bos_comp = [i ** 2 for i in range(1, 10)]

print('============== Soru 2 ===========================')


# SORU - 2
# Parametre olarak cümlelerden oluşan bir paragraf listesi alan bir fonksiyon yazın.Adı cumleleri_ver olsun.
# Fonksiyon bu paragraf listesi içindeki cümleleri dönsün
# önce for döngüsünü sonra compreherision ile yapınız.

def cumleleri_ver(liste):
    bos_liste = []
    for i in liste:
        bos_liste.append(i)
    return bos_liste


def cumleleri_ver_comp(liste):
    bos_liste = [i for i in liste]
    return bos_liste


paragraph = ["Lorem ipsum dolor sit amet, conectetur adipiscing elit",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse",
             "Excepteur sint occaecat cupidatat non proident."]
print(cumleleri_ver_comp(paragraph))


# SORU - 3
# Soru 2'deki paragrafı alıp bu sefer tüm cümlelelerdeki tüm kelimeleri tek bir liste içinde dönen bir fonksiyon yazalım
# Önce for sonra comp ile yapalım.

def kelimeleri_ver(liste):
    bos_liste = []

    for i in liste:

        for kelime in i.split():
            bos_liste.append(kelime)
    return bos_liste


print(kelimeleri_ver(paragraph))


# Comp ile yapalım

def kelimleri_ver_comp(paragraf):
    bos_liste = [j for i in paragraf for j in i.split()]

    return bos_liste


print(kelimleri_ver_comp(paragraph))

print('============= Soru 4 ======================')


# SORU - 4
# Soru 2' deki paragrafı alıp b sfer tüm cülelerdeki sadece sesli harfle başlayan kelimeleri tek bir liste içinde dönen bir fonksiyon yazın.
#  Önce for sonra comp ile yazın.

def sesli_kelimeleri_ver(liste):
    sesliler = ['a', 'e', 'i', 'ı', 'u', 'ü']
    bos_liste = []

    for i in liste:
        for j in i.split():

            if j[0].lower() in sesliler:
                bos_liste.append(j)

    return bos_liste


def sesli_kelimleri_ver_comp(liste):
    sesliler = ['a', 'e', 'i', 'ı', 'u', 'ü']
    bos_liste = [j for i in liste for j in i.split() if j[0].lower() in sesliler]
    return bos_liste


print(sesli_kelimleri_ver_comp(paragraph))

print('============= Soru 5 ======================')


# SORU - 5 :
# Sıfırdan 20'e (dahil) kadar olan tüm sayıların karesini alan bir fonksiyon yazın.
# Fonksiyon kareleri bir dict olarak dönsün dict'in keyi sayının kendisi  value ise karesi olsun.
# Direk comp ile yapalım

def kareler_sozlugu():
    bos_sozluk = {i: i ** 2 for i in range(0, 21)}
    return bos_sozluk


print('============= Soru 6 ======================')


# SORU - 6
# Parametre olarak bir sözlük alan bir fonksiyon yazın.
# Parametre olarak gelen sözlük şu şekilde olacak

# {
# 1 : ['Aziz Vefa',24
# 2 : [ 'Kaiser Soze',100]
# 3 : ['Zozo The Kid',45]
# 4 : ['Jonny Lash' , 70]
# }
# Fonksiyonunuz sadece numaraları ve adları alarak yeni bir sözlük yaratıp dönsün
# Önce for sonra comprehension ile yapınız.

def numaralar_ve_adlari(ogrenci_bilgileri):
    bos_liste = {}

    for key, value in ogrenci_bilgileri.items():
        bos_liste[key] = value[0]

    return bos_liste


def numaralar_ve_adlar_comp(ogrenci_bigileri):
    return {key: value[0] for key, value in ogrenci_bigileri.items()}


ogrenci_bilgileri = {
    1: ['Aziz Vefa', 24],
    2: ['Kaiser Soze', 100],
    3: ['Zozo The Kid', 45],
    4: ['Jonny Lash', 70]
}

print(numaralar_ve_adlar_comp(ogrenci_bilgileri))


# Parametre olarak bir sözlük alan bir fonksiyon yazın.Adı tek_numarali_adlar olsun
# Parametre olarak bir önceki sorudaki sözlüğü kullanın
# ipuçları dongu kullanmayın.
# direk comprehension ile yapın

def tek_numarali_adlar(liste):
    return {key: value[0] for key, value in liste.items() if key % 2 != 0}


print(tek_numarali_adlar(ogrenci_bilgileri))


# SORU - 8
# Parametre olarak ingilizce bir metin alan bir fonksiyon yazınız.Fonksiyonun adı kelime_uzunlukları olsun
# Fonksiyon iki liste dönsün. Listelerden biri kelimeleri içersin.Diğer liste ise kelime uzunlarını içersin.
# Eğer kelime ('the','in','as','at') kelimelerinden biri ise onu almasın.
# İpuçları
# Bir fonksiyon nasıl iki liste döner ? --> Tuple
# Döngü kullanmayın direk comp ile yapın.

def kelime_uzunluklari(metin):
    yasaklı_kelimeler = ('the', 'in', 'as', 'at')

    kelimeler = [kelime for kelime in metin.split() if kelime not in yasaklı_kelimeler]
    uzunluk = [len(kelime) for kelime in metin.split() if kelime not in yasaklı_kelimeler]

    return (kelimeler, uzunluk)


metin = 'It takes all the running you can do, to keep in the same place.If you want to get somewhere else, you must run at least twice as fast as that'

print(kelime_uzunluklari(metin))


# SORU - 9
# Parametre olarak bir sayı listesi alan bir fonksiyon yazın. Adı sadece_pozitifler olsun
# Fonksiyon liste içinden sadece pozitif sayıları alsın, tam sayı yapsın ve yeni bir liste dönsün.
# Comprehension ile yapın

def sadece_pozitifler(sayilar):
    return [int(sayi) for sayi in sayilar if sayi > 0]


sayi_listesi = [12.8, -27.2, -34.5, 58.4, -82.0, 66.6, 14.9]

print(sadece_pozitifler(sayi_listesi))

# SORU - 10
# Parametre olarak içinde listeler olan, iki seviyeli bir liste alan bir fonksiyon yazın. Adı listeyi_duzlestir olsun
# Fonksiyon listenin altındaki tüm listeleri düzleştirip geriye ek seviyeli  bir liste dönsün.
# Comprehension ile yapın

def listeyi_duzlestir(liste):

    return [x for i in liste for x in i ]

listeler_listesi = [[8,6],[3,1,4],[2,0,9],[5]]

print(listeyi_duzlestir(listeler_listesi))