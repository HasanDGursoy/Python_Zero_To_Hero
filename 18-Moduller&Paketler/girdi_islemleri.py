"""
Bu modul, kullanıcıdan bir girdi ister

"""


def girdi_iste():
    return input('Lütfen bir giriniz : ')


def string_al():
    """
    Kullanıcıdan bir metin ister ve bu metni döner
    :return: str tipinde bir girdi metni
    """
    girdi = girdi_iste()
    return girdi


def tam_sayi_al():
    while True:

        try:
            girdi = string_al()
            sayi = int(girdi)
        except ValueError:
            pass
        else:
            return sayi

def ondalik_sayi_al():

    # ondalıklı sayıyı kullanıcıdan alana kadar devam edelim
    while True:
        try:
            girdi = string_al()
            sayi = float(girdi)
        except:
            print('Ondalıklı sayı dedik be bro yapma böyle şeyler')
            continue

        else:
            return sayi


