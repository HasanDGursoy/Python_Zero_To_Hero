# LIST
# List bir dizidir.
# List'de bir dizi tipidir.
# Listlerde de 'index' yapısı ile içindekilere erişilebilir.
# Listler '[]' ile gösteririlir.

listem = [10, 20, 30, 40]
print(listem)

ucgenler = ['eşkenar', 'ikizkenar', 'çeşitkenar']

karma_liste = ['mail', 2.0, 5, True, False]

ic_ice_liste = ['sehir', ['ankara', 'istanbul'], [6, 34]]

bos= []
print(type(bos))

print('1 = ',ic_ice_liste[0])
print('2 = ',ic_ice_liste[1])
print('3 = ', ic_ice_liste[2])


print("=================================================")

# Listler Değiştirilebilir (Mutable)

peynirler = ['Ezine','Hellim','Tulum']
peynirler[0] = "Tel Peyniri"  # Değiştir çünkü listeler mutable :D
print(peynirler)
print("==============================================================")


# LİSTE ÜZERİNDE DÖNME

for peynir in peynirler:

    print(peynir)

print("==============================================================")

for index,peynir in enumerate(peynirler):
    print(" {0} : {1} ".format(index,peynir))

# Liste içinde dönerken elemanları değiştirebilirsiniz.

sayi_dizi=[10,20,30,40]
sayilar = [1,2,3,4]

for sayi in sayilar:
    sayi *= 10
    print(sayi)
    # ancak bu sayiları değiştirmez.

print("==============================================================")

# Listenin kendisini değiştirmek için -> index
# listeyi index ile update et

for index,sayi in enumerate(sayilar):

    sayi = sayi * 10

    sayilar[index] = sayi
    print(sayilar)
print("==============================================================")
# Her bir peynir isminden sonra 'Peyniri' kelimesini ekleyelim

peynirler = ['Ezine','Hellim','Tulum']

for index,peynir in enumerate(peynirler):

    peynirler[index] = peynir + " Peyniri"

print(peynirler)
















