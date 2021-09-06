# WHİLE DÖNGÜSÜ

n = 10

while (n > 0):
    print(n)
    n -= 1

# 1 - 20 kadar tek sayıların karelerini bulalım.

x = 1

while x <= 20:
    if x % 2 != 0:
        print(f"{x}'in karesi {x ** 2}")
    x += 1

# 1 - 10 arası çift sayıların toplamı

x = 0
deger = 0
while x <= 10:

    if x % 2 == 0:
        deger += x
        print(f" x = {deger}")
    x += 1

# Girilen sayı asalmı
is_prime = True
girdi = int(input("Lütfen bir sayı giriniz : "))
i = 2

while i < girdi:
    if girdi % i == 0:
        is_prime = False
   
    i += 1

if is_prime:
    print("Girdiğiniz sayı asaldır.")
else:
    print("Girdğiniz sayı asal değildir.")
