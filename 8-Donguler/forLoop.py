# FOR DÖNGÜSÜ

for i in range(10):
    print(i)

# Belirli bir aralıkda döner - > range(başlangıç,bitiş)
# başlangıç -> dahil
# bitiş -> dahil değil
print("=====================================================")
for i in range(1, 10, 2):  # Birden ona kadar 2 şer 2 şer ilerle demek
    print(i)

# Girilen bir sayının tüm çarpanlarını yazalım.

sayi = int(input("Lütfen bir sayı giriniz :"))

for i in range(2, sayi):
    if sayi % i == 0:
        print(i)

# Girilen bir sayının asal olup olmadığını bulalım.

deger_tutucu = 0
for i in range(2, sayi - 1):

    if sayi % i == 0:
        deger_tutucu+=1

if deger_tutucu >0:
    print("Girdiğiniz sayı asal değildir.")
else :
    print("Girdiğiniz sayı asaldır.")

# Tek for döngüsü içinde, 20 den 1'e kadar tek sayıları geriye doğru yazdır.

for i in range(20,0,-1):
    if i % 2 == 1:
        print(i)

