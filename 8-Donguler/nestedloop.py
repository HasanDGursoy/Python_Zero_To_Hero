# NESTED LOOPS - DÖNGÜ İÇİNDE DÖNGÜ

# Ekrana yıldızlardan oluşan bir kare çizelim

i = 0

while i < 3:
    yildizlar = ""

    j = 0
    while j < 3:
        yildizlar += "* "
        j+=1

    print(yildizlar)

    i+=1

# Bu sefer for ile yapalım
print("============================================")


for i in range(0,5,1):
    kare =""
    for j in range(0,6,1):

        kare +="* "
        


    print(kare)
