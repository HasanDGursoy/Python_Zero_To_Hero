# TUPLE
# Tuple Yaratmak
# Aynı string ve list gibi tuple da bir dizi (sequence) tipinde bir değişkendir.
# Tuple'lar hergangi bir türde değer alabilir ve tam sayılar ile indexlenirler.
# Dolayısı ile listlere çok benzerdirler.
# Tuple ile list arasındaki en önemli fark; List Mutable Tuple ise Immutable'dır.
# Tuple virgül ile ayrılmış bir listedir.


# Virgül ile ayrılmış değer girerek Tuple yaratmak

t = 'x','y','z','q','p'
print(t)
print(type(t))

t2 = (1,2,3,4,5,6)

print(isinstance(t2,tuple))

# Tek elemanlı tuple nasıl yaratırız.

tek_elemanli_tuple = ('x',) # sona virgül koy tuple olur.
print(type(tek_elemanli_tuple))

# tuple() Constructor'ı ile Tuple Yaratmak

t = tuple()
print(isinstance(t,tuple))

# Tek elemanlı yaratmak
tek = tuple('t')
print(type(tek))


# tuple() methoduna list verirseniz dizi tipinde her elemanı string de dahil ayrı bir tuple elemanı haline getirir.
# Çok elemanlı yaratmak
dil  = tuple('Python')
print(dil)

listem = ['A','B','C','D']

print(tuple(listem))


# List Operasyonlarının çoğu Tuple içinde geçerlidir.

# index varsa slicing işlemide vardır.

tup = ('t','u','p','l','e')
print(tup[1:4])

# cümleyi tersden çevirme

ay = tuple('Ay dünyanın uydusudur.')
print(ay)

# bu cümleden dünya kelimesini alalım.

print(ay[3:8])

print(ay[::-1])

# Tuple'lar Immutable (Değiştirilemezler)
# bir şeyi değiştirmek istiyorsak yeniden atamak zorunda kalırız.

# mesela

#ay[3] = 'haha'
# bunu yapamayız
# o yüzden tekrar atamak zorunda kalırız. :S

# TUPLE KARŞILAŞTIRMA

print((1,2,3)< (5,4,3))

# int lerde ilk sayıya bakıyor
# stringlerde bütün değerleri tek tek dolaşıyor
# alfabetik sırayla inceliyor.

a,b,c,d = ['Python','Java','JavaScript','C#']
print(a,b,c,d)
