# İç İÇE FONKSİYONLAR
# Nested Functions

# İç içe fonksiyonlar kullanıp bir sayının 5 in ve 8 in ortak katı olup olmadığını bulalım


def ortak_kat_mi(n):
    """
    Fonksiyon girilen sayının 5 ve 8 in ortak katı ise True Döncek.
    """

    def besin_kati(n):
        if n % 5 == 0:
            return True
        else:
            return False

    def sekin_kati(n):
        if n % 8 == 0:
            return True
        else:
            return False

    if sekin_kati(n) and besin_kati(n):
        return True
    else:
        return False

bolen = ortak_kat_mi(80)
print(bolen)
