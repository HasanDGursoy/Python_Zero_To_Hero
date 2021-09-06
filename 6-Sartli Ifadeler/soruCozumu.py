# 1 - Kullanıcı tarafıdan girilen bir sayının tek mi çift mi olduğunu bulun.

girdi = input("Lütfen sayı giriniz : ")

if girdi.isdigit():
    sayi = int(girdi)
    if sayi % 2 == 0:
        print("SAYİ ÇİFT")
    else:
        print("SAYİ TEK")

# 2 - Kullanıcı tarafından girilen harfin sesli mi yoksa sessizmi olduğunu konrol edin.

harf = input("Lütfen bir harf giriniz : ")

if harf == "a" or harf == "e" or harf == "i" or harf == "ı" or harf == "o" or harf == "ö" or harf == "u" or harf == "ü":
    print("Girdiğiniz harf seslidir.")
else:
    if len(harf) > 1 or harf.isdigit():
        print("Yanlış değer girdiniz!")
    else:
        print("Girdğiniz harf sessizdir.")


# 3 - Kullanıcı tarafından girilen kenar sayısına göre hangi şekil olduğunu bulan bir fonksiyon yazın.

def sekil_bul():
    n = input("Bir kenar sayısı giriniz : ")

    n = int(n)

    if (n == 3):
        print("Şekil Üçgendir.")
    elif (n == 4):
        print("Şekil Dörtgen yada Karedir.")
    elif (n > 4):
        print("Şekil çokgendir uğraşamam yazmak için")
    else:
        print("Şekilsiz garip bir şeydir.")


sekil_bul()


# 4 - Kenar uzunlukları verilen bir bir üçgene adını ekrana yazan bir fonksiyon oluşturalım.

def ucgen_adi():
    ad = ""

    kenar1 = float(input("Birinci kenar uzunluğunu giriniz : "))
    kenar2 = float(input("İkinci kenar uzunluğunu giriniz : "))
    kenar3 = float(input("Üçüncü kenar uzunluğunu giriniz : "))

    if kenar1 == kenar2 and kenar2 == kenar3:
        ad = "Eşkenar Üçgen"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        ad = "İkizkenar Üçgen"
    else:
        ad = "Çeşit Kenar Üçgen"

    return ad


ucgen_yazdir = ucgen_adi()
print(ucgen_yazdir)


# Kullanıcıdan iki sayı alalım. Bu sayılardan hangisinin küçük hangsinin büyük olduğunu bulalım
# Sonra büyük sayıdan geriye gidip, küçük sayıya kadar olan tüm çift sayıları ekrana yazdıralım.

def geri_say():
    sayi1 = int(input("Birinci Sayı :"))
    sayi2 = int(input("İkinci Sayı : "))

    buyuk_sayi = 0
    kucuk_sayi = 0

    if sayi1 > sayi2:
        buyuk_sayi = sayi1
        kucuk_sayi = sayi2
    else:
        buyuk_sayi = sayi2
        kucuk_sayi = sayi1

    print(buyuk_sayi)
    print(kucuk_sayi)
    geri_say_1(kucuk_sayi,buyuk_sayi)

def geri_say_1(bitis,deger):

    if (bitis == deger):
        print(bitis)
        return
    else:
        print(deger)
        geri_say_1(bitis,deger-1)

geri_say()

