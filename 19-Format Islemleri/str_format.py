"""
2- str.format()

{} ile string formatlama

"""
# index vermeden yapalım
selam = 'selam sana {} {}'
print(selam.format('Peter', 'Parker'))

# index vererek
ifade = "{0} kelimesinin {1} adet harfi var"
print(ifade.format("Python", len("Python")))

# isim vererek
adi_nereden_gelir = "{ad} ismi {kaynak} gelir"
print(adi_nereden_gelir.format(ad='Python', kaynak='Monthy Python dan'))

print(adi_nereden_gelir.format(ad='Java', kaynak='Endonezyada ki kahve türündenden'))

