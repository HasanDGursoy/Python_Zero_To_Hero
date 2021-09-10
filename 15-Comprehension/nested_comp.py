# İÇ İÇE COMPREHENSİON (NESTED)
# Verilen iki listeyi birleştirip, içinde tüm ikili kombinasyonları, Tuple olarak tutan yeni bir liste yaratalım.

harfler = ['A', 'B']
sayilar = [1, 2, 3]

sonuc = []

for harf in harfler:
    for sayi in sayilar:
        tup = (harf, sayi)
        sonuc.append(tup)
print(sonuc)

# comprehension

sonuc_comp = [(harf, sayi)
              for harf in harfler
              for sayi in sayilar]
print(sonuc_comp)

# 1-10 arası olan sayıları, kendileri key ve kendinden küçük pozitif tam sayilar da value listesi olacak şekilde dict Kuralım.

# klasik yöntem

bos_dict = {}

for i in range(11):
    for j in range(1, i + 1):

        if i not in bos_dict:
            bos_dict[i] = [j]
        else:
            bos_dict[i].append(j)
print(bos_dict)

# comprehension

dict_comp = {i: [j for j in range(1, i + 1)]
             for i in range(1, 11)}
