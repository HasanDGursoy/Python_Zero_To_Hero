# LIST SLICING - LİSTE DİLİMLEME

liste = ['a', 'b', 'c', 'd', 'e', 'f']

print(liste[2:5])
print(liste[0:4])
print(liste[0:])

# Liste Kopyalamak list[:] = Bu kopyala demektir.

yeni_liste = liste[:]
yeni_liste
print(yeni_liste)

baska_liste = liste[:]
baska_liste
print(baska_liste)

# Liste 1 ve 2 elemanlarını değiştir.

liste[1:3] = ['hasan', 'mehmet']
print(liste)

# ID YONTEMI
# Python'da tüm nesneler bir 'id' ile tutulur
# ID degeri -> id() fonksiyonu ile bulunur.

# Liste değişkenlerin ıd sini alalım.
print(id(liste))
print(id(yeni_liste))
print(id(baska_liste))