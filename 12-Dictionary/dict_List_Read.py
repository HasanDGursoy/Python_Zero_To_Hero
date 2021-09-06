# DİCT ELEMAN OKUMA

# Bunun için 'dict.items()' fonksiyonunu çağırmak yeterli
# Sadece anahtarlar için 'dict.keys()' ve sadece değerler için 'dict.values()'

ingTR = {
    'name': 'ad',
    'foot': 'ayak',
    'old': 'yas',
    'identy': 'kimlik',
    'minority': 'azınlık',
    'majority': 'çoğunluk'
}

# for ile key-value okumak

for key, value in ingTR.items():
    print("{0} keyinde : {1} değeri vardır.".format(key, value))

for k, v in ingTR.items():
    print(k, ' : ', v)

# Sadece key lerde gezmek.

for key in ingTR.keys():
    print(key)

# sadece değerler

for deger in ingTR.values():
    print(deger)

arac = {
    'marka': 'ford',
    'model': 'mustang',
    'yil': 1964,
    'renk': 'kırmızı',
    'fiyat': 300000
}

# get() kullanımı da vardır.
# get in güzel olan yeri olmayan birşeyi sorarsanız none hatası verir ve daha güvenlidir.
print(arac.get('model'))

# len()

print(len(arac))

# 'in' yapısı
# bu şekilde yazarsak key içinde arar.
print('yil' in arac)

# degerler içinde aramak istesek

print('dört' in ingTR.values())


