# RANGE FONKSİYONU İLE LİST ÜRETMEK

for i in range(1,30,2):
    print(i)

liste = [2,5,8,11,14,17,20,23,26,29]
# yukarıdaki gibi 3'er 3'er artan bir liste lazımdı diyelim
# bunu range ile yapabiliyoruz.
print(liste)
aralik = range(2,30,3)
range_list = list(aralik) # tam olarak bu şekilde range i de liste haline getirebiliyoruz.
print(range_list)

# 2'den başla 100' e kadar , 4'er artan sayılar

print(list(range(2,100,4)))