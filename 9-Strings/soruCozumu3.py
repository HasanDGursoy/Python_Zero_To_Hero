# SORU - 8 : Kullanıcıdan bir email adresi isteyiniz.
#          : Bu mail adresini, index yapısı kullanarak kullanıcı adı ve domain adı olarak ayırınız.
#          : Kullanıcı adı ve domain adı "@" karakteri ile ayrılır. Eğer email adresi "@" karakteri içermiyorsa, kullanıcıya "Uygunsuz email formatı" mesajı döndürünüz.


def email_ayir():
    email = input("Lütfen bir email giriniz : ")

    bolme_noktasi = email.find('@')  # varsa indexini döndürür.

    if bolme_noktasi == -1:
        print("Uygunsuz email formatı")
    else:
        print("Kullanıcı adı : ", email[:bolme_noktasi])
        print("Domain Adı : ", email[bolme_noktasi + 1:])


email_ayir()


# SORU - 9 : Aşşağıdaki şekilde bir fonksiyon yazınız.
#          : Kullanıcıdan bir cümle istesyin ve tersden yazdırıp yollayın.

def ters_yaz():
    iste = input("Bir metin giriniz : ")
    print(iste[::-1])
    return iste[::-1]


# SORU - 10 : Kullanıcıdan bir cümle içindeki her bir karakter alfabaden sıradaki karaker ile değiştiren fonksiyon yazın.

"""
Yapılacaklar

* iç içe fonksiyonlar kullanalım
* İçeride harf_kucuk_mu() ve harf_buyuk_mu() şeklinde harfin büyük yada küçük olduğunu veren fonksiyonlar yazalım.
* ilgili alfabe ve harf alıp , o alfabede o harfden sonra gelen harfi bulan, sıradaki_harf() fonksiyonu olsun.
 
"""


def siradaki_harfle_degistir():
    cumle = input("Lütfen bir cümle giriniz : ")

    alfabe_kucuk = "abcçdefgğhiıjklmnoöprsştuüvyz"
    alfabe_buyuk = "ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ"

    yeni_cumle = ""

    def harf_kucuk_mu(harf):
        return harf in alfabe_kucuk

    def harf_buyuk_mu(harf):
        return harf in alfabe_buyuk

    def siradaki_harf(alfabe, harf):
        index = alfabe.find(harf)
        return alfabe[index + 1]

    # cumle içindeki harfler üzerinde döngü kuralım

    for harf in cumle:
        if harf_kucuk_mu(harf):
            yeni_harf = siradaki_harf(alfabe_kucuk,harf)
        elif harf_buyuk_mu(harf):
            yeni_harf = siradaki_harf(alfabe_buyuk,harf)
        else:
            yeni_harf = harf

        yeni_cumle +=yeni_harf
    print(yeni_cumle)

siradaki_harfle_degistir()