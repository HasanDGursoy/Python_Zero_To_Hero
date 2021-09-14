"""
try- except

try:

    ....
    ....
    ....
except:
    ....
    ...
    ...

try :
    -kodu çalıştırmaya çalışır
    -hata yoksa, try'in sonuna kadar gelir
    -hata varsa, kod try'dan çıkar
except:
    -eğer try içinde hata almışşa, except'e gelir
    -derleyici hata olan yerden except içine atlar
    -yani hatanın yakalandığı yer except bloğudur.

"""


# Örnek:
# hatanın yönetilmediği durum
def karesini_al():
    girdi = input('Lütfen bir tamsayı giriniz : ')
    sayi = int(girdi)
    print(sayi)


# karesini_al()

def karesini_hesapla_try():
    try:
        girdi = input('lütfen bir tam sayı giriniz : ')
        sayi = int(girdi)
        print(sayi ** 2)
    except:
        print('sayı girmediniz')


# karesini_hesapla_try()

def karesini_hesapla_try_again():
    try:
        girdi = int(input('Lütfen bir tam sayı giriniz : '))
        sayi = girdi ** 2
        print(girdi)

    except:
        print('Sayı girmediniz..')
        karesini_hesapla_try_again()


karesini_hesapla_try_again()


# Örnek
# olmayan bir dosya açmaya çalışalım
def dosya_ac(dosya_yolu):
    dosya = open(dosya_yolu)

    # satır satır
    for satir in dosya:
        print(satir.split())


# aynı klasör (dizin) içindeki bir dosyayı okumak için
yol = 'diziler.txt'


# dosya_ac(yol)

# hata yönetimi ile deneyelim şimdi

def dosya_ac_try(dosya_yolu):

    try:
        dosya = open(dosya_yolu)

        for satir in dosya:
            print(satir.split())
    except:
        print('Malesef dosya bulunamadı')

yol = 'diziler.txt'
dosya_ac_try(yol)

"""
Birden fazla hata olması durumu : 
* Birden fazla except bloğu ile
"""
# örnek :

def bolme_try():
    try:
        bolunen = int(input('Lütfen bölüneni giriniz : '))
        bolen = int(input('Lütfen böleni giriniz : '))

        bolum = bolunen/bolen
        print(bolum)
    except ValueError:
        print('Tam sayı girmediniz')
    except ZeroDivisionError:
        print('Bölen sıfır olamamaz.')

bolme_try()