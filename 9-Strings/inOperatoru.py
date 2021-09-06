# in OPERATÖRÜ
# Bir karakter yada metin başka bir metin içinde olup olmadığını kontrol eder.
# var ise True döner

agac = "ahlat ağacı"
at = "at"
print(at in agac)
print("s" in agac )


# kullanıcadan alınan değere göre içinde a varmı yok mu kontrol ediyorz.

metin = input("Lütfen bir metin giriz : ")

def a_var_mi(metin):

    for harf in metin:
        if harf =="a":
            print("Metinin içinde a var.")
        else:
            print("yokkk")
a_var_mi(metin)

# kısa yol

def a_varmidir(metin):

    if "a" in metin:
        print("varrrrr")
    else:
        print("yokkkkkk")
    return "a" in metin
a_varmidir(metin)
    # kod kısalığına bakın :D
