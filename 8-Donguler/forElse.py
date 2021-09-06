# FOR - ELSE YAPISI
# Bazen bir for döngüsünün düzgün tamamlanıp tamamlanmadığını kontrol etmeniz gerekebilir.
# Eğer bir for döngüsü bir elemanı için çalışmamışsa , 'break' ifade çağrılmışsa, ozaman düzgün çalışmamış demektir.
# Bunun için for-else yapısı  kullanılır.
### Döngü kesintiye uğramassa çalışan bir uygulama metodu.
# 2 ile 10 arasındaki sayıları yazdırdığımızı var sayalım.
# Eğer sayı 7'nin katı ise, döngüden çıkalım.
# Eğer düzgün çalışırsa "Döngü düzgün Çalıştı" yazalım.

print("--------------- For Döngüsünden Önce -----------------")

for i in range(2, 10):
    print(i)
    if i % 7 == 0:
        break
else:
    print("Döngü düzgün çalıştı")
print("--------------- For Döngüsünden Sonra ----------------")

print("--------------- For Döngüsünden Önce -----------------")

for i in range(2, 10):
    print(i)
    if i % 17 == 0:
        break
else:
    print("Döngü düzgün çalıştı")
print("--------------- For Döngüsünden Sonra ----------------")
