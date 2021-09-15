"""
modul : .py ile biten Python dosyasıdır
"""

# ilk modülümüzü import edelim
import ilk_modulumuz

# peki bu modulumuzde bir fonksiyon olsaydı
ilk_modulumuz.selamla()

"""
Girdi işlemleri için modul yazalım.
"""
import girdi_islemleri

deger = girdi_islemleri.girdi_iste()
print(deger)

metin = girdi_islemleri.string_al()
print(metin)

sayi_degeri = girdi_islemleri.tam_sayi_al()
print(sayi_degeri)

ondalikli = girdi_islemleri.ondalik_sayi_al()
print(ondalikli)