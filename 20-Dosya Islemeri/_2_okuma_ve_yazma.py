"""
Okuma - Yazma

Okuma Metotları :
* read()  --> tüm dosyayı tek seferde okur
* readline() --> Sadece tek satır okur, bir alt satıra geçer ve bekler
* readlines() --> kalan tüm satırları okur
"""

# Okuma Örnekleri

# with open('lorem.txt',mode='rt',encoding='utf-8') as lorem:
#     yazi = lorem.read()
#    print(yazi)

# ilk 50 karakteri okuyalım

# with open('lorem.txt', mode='r', encoding='utf-8') as lorem:
#     yazi_50 = lorem.read(50)
#     print(yazi_50)

# lorem ipsum dosyasını satır satır oku
# with open('lorem.txt') as lorem:
#     satir_1 = lorem.readline()
#     satir_2 = lorem.readline()
#     satir_3 = lorem.readline()
#     print(satir_1,satir_2,satir_3)


# bütün dosyayı satır satır readline ile oku

# with open('lorem.txt') as lorem:
#     for satir in lorem:
#         print(satir.split())  # \n karakterinden parçalar, sonrada ' ' siler.

"""
Yazma İşlemleri :
* w --> write : boş dosya olarak açar (dikkat) çünkü siliyor.
* a --> append : mevcut dosyaya ekleme yapar.
"""

# w ile aç
# with open('lorem.txt', mode='w', encoding='utf-8') as lorem:
#    lorem.write('Yeni Satır')

# şimdi a ile silmek yerine direk ekleme yapıcaz.
# with open('lorem.txt',mode='a',encoding='utf-8') as lorem:
#    lorem.write('\n yeni satır 2222')

# birden fazla satır ekleyelim
with open('lorem.txt', mode='a', encoding='utf-8') as lorem:
    eklenecek_satirlar = ['\nEk satır 1', '\nEk satır 2', '\nEk satır 3']
    lorem.writelines(eklenecek_satirlar)
