# COMP İÇİNDE İF-ELSE YAPISI
# Alıştırma :
# 1-20 arası tek sayıları önce döngü sonra comprehension
bos_list = []
for i in range(21):

    if i % 2 != 0:
        bos_list.append(i)
print(bos_list)

# Comprehension

tekler_comp = [i
               for i in range(21)
               if i % 2 == 1]

# Alıştırma

# 2-20 arası tüm sayıları kendileri key olacak ve çarpanları da bir value listesi olacak şekilde bir dict içine koyalım.

bos_dict = {}

for i in range(2, 20):
    for j in range(2, i + 1):
        if i % j == 0:
            if i not in bos_dict:
                bos_dict[i] = [j]
            else:
                bos_dict[i].append(j)
print(bos_dict)

# Comprehension

bos_comp = {i: [j for j in range(2, i + 1) if i % j == 0]
            for i in range(2, 22)

            }
# Alıştırma
# 2-20'ye kadar olan tüm çift sayıları, kendileri key olacak ve çarpanları da bir valu olacak şekilde bir Dictionary yaratalım.

# klasik yol

carpanlar = {}

for i in range(2, 21, 2):

    for j in range(2, i + 1):

        if i % j == 0:
            if i not in carpanlar:

                carpanlar[i] = [j]
            else:
                carpanlar[i].append(j)

print('=================================')
# compreherision ile kullanılan yol

carpanlar = {i: [j for j in range(2, i + 1) if i % j == 0]
             for i in range(2, 21, 2)}
print(carpanlar)

# NOT :
# Mümkün olan hemen her yerde Compreherision kullanın.(for loop yerine)
# Performans sağlar
# Kodunuz daha sade ve okunur olur
