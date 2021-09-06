# MATRİS OPERASYONLARI

# Python'da bir liste içinde başka şisteler bulundurabilir.
# Buna İç İçe Listeler (Nested List) denir.

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(a[0][2])

# MATRİSLERİN TOPLANMASI
# Matrislerde toplama eleman bazlı olması lazım.


b = [[2, 3, 5], [6, 7, 9], [0, 6, 4]]

c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# Matrislerin elemanları üzerinde dönme

for i in range(len(a)):  # satır sayısı

    for j in range(len(b)): # satır sayısı

        c[i][j] = a[i][j] + b[i][j]
print(c)