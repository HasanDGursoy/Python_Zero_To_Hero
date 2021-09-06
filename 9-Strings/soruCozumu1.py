# SORU - 1 : Verilen bir metnin bütün kelimelerinin baş harflerini büyük, diğer harflerini küçük yapan bir fonksiyon yazın
metin = "makine öĞrENMesi güzEldiR"
def harf_buyult(metin):

    yeni_metin= metin.lower().title()


    print(yeni_metin)
harf_buyult(metin)

# SORU - 2 : Parametre olarak bir metin, birde harf alan bir fonksiyon yazın
#          : Fonksiyonunuz verilen metin içinde, verilen harfden kaç tane varsa yazdır.

def metin_say(metin,harf):

    return metin.count(harf)

deger =metin_say(metin,"e")
print(deger)

# SORU - 3  : Kullanıcıdan bir cümle isteyin. Bu cümle içinde ki her bir harfin kaç sefer geçtiğini print edin

def harfleri_say():

    cumle = input("Lütfen bir cümle giriniz : ")

    yazilan_harfler = ""

    for harf in cumle:
        if harf == " ":
            continue
        adet = metin_say(cumle,harf)

        if not harf in yazilan_harfler:
            print("{0} harfi {1} defa geçiyor. ".format(harf,adet))
            yazilan_harfler +=harf

harfleri_say()

