# LİSTE OPERASYONLARI
# Listlerde +, * (artı ve çarpma) gibi işlemleri yapabilir.z
# Ama kendi mantığı içerisinde.

# '+' operatörü

a = [10, 20, 30]
b = [4, 8, 12]
c = a + b
print(c) # içindeki değerleri toplamadı uc uca ekledi.

hafta_ici = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma']
hafta_sonu = ['Cumartesi','Pazar']

hafta = hafta_ici + hafta_sonu
print(hafta)

# '* ' Çarpma operatörü
# Verilen listeyi verilen miktarda tekrarlar.

print([5]*3)
print([11,12]* 4)
print(hafta * 5)