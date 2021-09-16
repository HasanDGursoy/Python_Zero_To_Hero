"""
sesli harfleri dönen bir fonksiyona sahiptir.

"""


def sesli(metin):
    liste = ['a', 'e', 'i', 'ı', 'u', 'ü', 'o', 'ö']

    bos_liste = []

    for harf in metin :
        try:
            if harf in liste:
                bos_liste.append(harf)
        except:
            raise
    return set(bos_liste)