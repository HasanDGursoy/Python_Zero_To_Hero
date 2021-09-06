deger = int(input("Sayı giriniz : "))


# SORU - 5 : Ekrana yıldızlardan oluşmuş ters bir ikizkenar dik üçgen çizen bir fonksiyon yazın.
# Fonksiyon parametre olarak üçgenin dik bir kenarında bulunan yıldız sayısını alsın. Ters dik üçgen olacak.!!!

def ters_ucgen_for(deger):
    for i in range(deger):

        ucgen = ""
        for j in range(deger - i):
            ucgen += "* "
        print(ucgen)


ters_ucgen_for(deger)


# SORU - 6 : Ekrana ilk önce düz ikizkenar kenar üçgen daha sonra ters ikiz kenar üçgen çizcez.

def duz_ters_ucgen(deger):
    for i in range(deger):
        ucgen = ""
        for j in range(i):
            ucgen += "* "

        print(ucgen)

    for ii in range(deger):

        ucgen = ""
        for jj in range(deger - ii):
            ucgen += "* "
        print(ucgen)


duz_ters_ucgen(deger)


# SORU - 7 : Parametre olarak kendisine verilen bir sayının asal sayı olup olmadığını dönen bool bir fonksiyon yazınız.

def asal_mi(deger):
    counter = 0
    for i in range(3, deger, 1):
        if deger % i == 0:
            counter += 1
    print(counter)
    if counter > 0:
        print("Girdiğiniz sayı asal değildir.")
    else:
        print("Girdiğiniz sayı asaldır.")


asal_mi(deger)

# SORU - 8 : Parametre olarak kendisine verilen bir sayının bütün asal çarpanlarını bulan bir fonksiyon yazın.
metin = int(input("Lütfen bir sayı giriiz: "))
def asal(metin):

    asal = True

    for i in range(2,metin):
        if metin % i ==0:
            asal = False
    return asal
ss=asal(metin)
print(ss)
def asal_bul(metin):
    for i in range(2, metin):
        if metin % i == 0:

            if asal(i):
                print(i)


asal_bul(metin)


