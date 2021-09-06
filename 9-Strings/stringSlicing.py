# STRİNG SLİCİNG - METİN DİLİMLEME

# dizi[baslangıc: bitis : artış]
# başlangıç boş bırakılırsa default olarak 0 dır.
# bitiş değerini boş bırakırsak default olarak dizinin son index'idir.
# artış boş bırakılırsa default olarak bir dir.
# başlangıç dahildir. bitiş dahil değildir. metin[0,5] ise 0 dahildir 5 den bir önceki deger dahildir.

s = "derin öğrenme"

print(s[0:5])
print(s[:5])
print(s[6:13])
print((s[6:]))

rakamlar = "123456789"
tekler = rakamlar[::2]
print(tekler)
ciftler = rakamlar[1::2]
print(ciftler)
print(rakamlar[::])

# TERS SLİCİNG - (NEGATİF İNDEX) METİNİ TERS DİLİMLEME

# dizi [bitiş: başlangıç : -artış ]
# sondan başa doğru gelir.
# son elaman index = -1 dir (0 unut artık o yok.)

sayilar = "123456789"
metin = "hasan doğacan gürsoy"
print(sayilar[::-1])  # Sayıyı komple tersden yazdırdı.
print(sayilar[-1])  # sondaki index alır.
print(sayilar[6], sayilar[-7])
print(metin[:-1])

# rakamları sondan başa 2 şer atlayarak yazın.
print(sayilar[::-2])

# ters index ile 456 ve 654 dilimlerini alalım
# ters index de olsa index sağa doğru sayar.
print("============================")
print(sayilar[-6:-3:1])
print(sayilar[-4:-7:-1])

# 34567 ve 76543 sayısını ters index olarak yazdıralım
print(sayilar[-7:-2:1])
# ve
print(sayilar[-3:-8:-1])

# MİSSİON COMPLETED 







