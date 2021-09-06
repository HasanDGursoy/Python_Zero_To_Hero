# Is ifadesi

# x == y         --> Değer Kontrolü
# id(x) == id(y) --> Kimlik Kontrolü

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

# şimdi a ile b aynı nesne mi bakalım ?

print(a is b)  # false

s1 = 'bilgisiyar'
s2 = 'bilgisiyar'
print(s1 is s2)  # true

