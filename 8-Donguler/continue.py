# CONTİNUE - DÖNGÜNÜN BİR SONRAKİ ADIMINA ATLA

# 1 den 10 a kadar çift sayıları yazdıralım

for i in range(1, 11):

    if i % 2 == 1:
        continue
    else:
        print(i)

# Verilen metnin harflerini yazacağız ama boşluk görürsek yazmicaz.

metin  = input("Lütfen bir metin giriniz :")

for i in metin:
    if i == " ":
        continue
    else:
        print(i)