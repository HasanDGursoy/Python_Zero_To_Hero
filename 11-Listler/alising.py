# ALİSİNG (YENİ BİR AD VERME)

# Primitive tipler : int, float, string,boolean
# Non-Primitive tipler : list, dict, tuple

x = 24
y = x
print(x == y)
print(x is y)

y = 40

print(x == y)
print(x is y)

# Non - Primitive Tipler

a = [1, 2, 3, 4, 5, 6]
b = a

print(a == b)
print(a is b)

# Pirimitive Tipler -> yeniden atama

b = [10, 20, 30, 40]
print(a == b, a is b)
print(a)
print(b)
# peki sadece bir kısmını değiştirsek ne olurudu

a = [1,2,3,4,5]
b = a
print(a)
print(b)

b[0] = 'B'
b[1] = 'C'
print(a)
print(b)

# Mutasyon yukarıda görüldüğü gibi nesneleri ayırmaz.İkisininde değeri aynı anda değişir.
# O yüzden non-primitive tiplerde atama işlemi normal bir atama işlemi değil bir yeniden adlandırma işlemidir.
