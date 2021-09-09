# SETLERDE ELEMAN EKLEME
# Set'e Eleman Ekleme ==>> add()

notlar = ['a', 'b', 'c']
notlar = set(notlar)
notlar.add('Ğ')
notlar.add('I')
print(notlar)

# set'ten eleman çıkarmak : remove()

notlar.remove('I')
print(notlar)

# Set üzerinde For Döngüsü

for notcuk in notlar:
    print(notcuk)

# set'lerde Atama işlemi :
# Alising : Yeniden Adlandırma

a = {2, 5, 7}
b = a

b.add('YENİ')
# Şimdi a ve b yi yazdır
print('a : ', a)
print('b : ', b)

# identical : is
print(a is b)
print(a == b)

# şimdi a'ya eleman ekle
a.add('YYY')

# Set'e tek seferde, çok sayıda eleman eklemek : update()

meyveler = {'Elma', 'Armut', 'Kiraz'}
print(meyveler)
daha_cok = ['Çilek', 'Muz', 'Portakal']
meyveler.update(daha_cok)
print(meyveler)
