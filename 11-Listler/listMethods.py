# LIST METHODS
"""
* append() : Listenin sonuna yeni bir eleman ekler
* insert() : Belli bir index ile listeye eleman ekler
* extend() : Listeye başka bir liste ekler
* sort() : Listeyi belli bir sıraya göre sıralar. Listeyi değiştirir.
* sorted() : Listeyi sıralar ve sıralı olarak yeni bir liste verir.

"""
# Append()

harfler = ["a", "b", "c", "d", "e"]

harfler.append('Selam')
harfler.append('İyi')
harfler.append('Kötü')
print(harfler)
print("=============================================================")

# Insert()

print('insert öncesi harfler : ', harfler)
harfler.insert(2, 'benim adım name')
print('insertten sonra :', harfler)
print("=============================================================")

# Extend()

sesli_harfler = ["a", "e", "ı", "u", "o"]
noktali_sesler = ["i", "ü", "ö"]

sesli_harfler.extend(noktali_sesler)
print(sesli_harfler)

print("=============================================================")

# Sort()

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

# sort() -> default olarak (küçükden büyüğe sıralar.)
# 'reverse' parametresi ile sıralama yönü değiştirelebilir.

t.sort(reverse=True)
print(t)

print("=============================================================")

# Sorted()

a = [4, 3, 2, 12, 5, 16, 3]

b = sorted(a)
c = sorted(a, reverse=True)
print(c)