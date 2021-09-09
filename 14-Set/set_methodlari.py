# SET METHODLARI

# Kesişim
# iki set'in yani kümenin ortak elemanlarını bulmak için -> kesişim kümesi -> intersection

notlar = ['A', 'B', 'C', 'D', 'E']
dereceler = ['A', 'L', 'T', 'B', 'F']

notlar = set(notlar)
dereceler = set(dereceler)

print(notlar.intersection(dereceler))

# Birleşim
# union()

print(dereceler.union(notlar))

# Fark
# iki set arasındaki fark -> kümelerin farkı --> difference

print('notlar : ',notlar)
print('dereceler : ',dereceler)

# notlarda olup dereceler kümesinde olmayanlar.

print(notlar.difference(dereceler))


# issubset():
# Bir küme başka bir kümenin alt kümesimi ? issubset()
# notlar, derecelerin alt kümesimi

print(notlar.issubset(dereceler))

print(set({'F','L'}).issubset(dereceler))

# issuperset():
# bir küme başka bir kümenin üst kümesimi
print(dereceler.issuperset(notlar))
print(dereceler.issuperset(dereceler))

# symetric_diffrence():
# iki kümenin karşılıklı ayrık elemanları kümesi --> Symmetric Diffrence

print(notlar.symmetric_difference(dereceler))