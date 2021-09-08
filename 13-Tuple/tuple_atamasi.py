# TUPLE ATAMASI

a = 99
b = 1

# Yöntem 1 -> geçiçi atama

print('a', a)
print('b', b)

gecici = a

a = b
b = gecici

print('a', a)
print('b', b)

# Python'da 'Tuple Ataması' bu işlemi (swap) otomatik yapar.

a = 99
b= 1

a ,b = b ,a

# Alıştırma
# tuple ataması ile email içindeki kullanıcı adı  ve domain adını ayıralım

kullanici_adi,domain = 'johnsnow@got.com'.split('@')
print(kullanici_adi)
print(domain)
