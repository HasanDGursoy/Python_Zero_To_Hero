# 1 - Ekrana "Selam Dünya! " yazan bir fonksiyon yazın.
import math


def selam_dunya():
    print("Selam Dünya!")


selam_dunya()


# ================================================================================================================================================
# 2 - 2 tane String Parametre alın ve yazdırın Örnek : Selam clark kent ve superman. # Stringin Format fonksiyonunu kullanın.

def hi_man(name1, name2):
    print("Selam {0} ve {1}.".format(name1, name2))


hi_man("hasan", "züha")


# ================================================================================================================================================
# 3 - Kullanıcıdan girdi olarak ismini isteyen bir fonksiyon yazın. (Girdi almak için input() fonksiyonunu kullanın.)


def inp_al():
    name = input("Lütfen isminizi Giriniz: ")

    print("Selam sana " + name)


inp_al()


# ================================================================================================================================================
# 4 - Parametre olarak 3 sayı alan bir fonksiyon yazın. En büyüğünü geri döndürsün.Docstring de ekleyin

def max_sayi(num1, num2, num3):
    """
    Girilen üç tane sayıdan en büyüğünü yazdırır.
    max_num= max(num1,num2,num3)
    :param num1: int
    :param num2: int
    :param num3: int
    :return: max_value
    """
    max_num = max(num1, num2, num3)

    return max_num


yazdir = max_sayi(15, 20, 30)
print("Sayıların en büyüğü : " + str(yazdir))
help(max_sayi)
print(max_sayi.__doc__)


# ================================================================================================================================================
# 5 - Parametre olarak gelen metni parçalayan küçük harfe çeviren bir fonksiyon yazın.

def parcala_ve_kucult(orjinal_metin):
    # strip() --> içerisi boş ise boşluk karakterinden parçalar.
    parcalanmis_metin = orjinal_metin.strip()
    print(parcalanmis_metin)

    # lower
    kucultulmus_metin = parcalanmis_metin.lower()
    print(kucultulmus_metin)


parcala_ve_kucult("Selam sdaADASd Sana")


# ================================================================================================================================================
# 6 - Parametre olarak girilen iki sayının toplamını dönen bir fonksiyon yazınız.

def sum_fonksiyonu(num1, num2):
    toplam = num1 + num2

    print(toplam)


sum_fonksiyonu(15, 302)

# ================================================================================================================================================
# 7 - Parametre olarak gelen 3 sayı alan bir fonksiyon yazın. Sayıların ikili farklarını alın ama mutlak deger içinde sonrada en küçüğünü yazdırın.

def en_kucuk(n1,n2,n3):

    fark_1 = abs(n1-n2)
    fark_2 =abs(n1-n3)
    fark_3 =abs(n2-n3)

    # En küçük farkı dön
    return min(fark_3,fark_2,fark_1)
min = en_kucuk(10,30,50)
print(min)

# ================================================================================================================================================
# 8 - Parametre olarak sayı alan ve bunun kare kökünü döndüren sayı yazınız.

def kara_kok(num):

    num = int(math.sqrt(num))

    print(num)
kara_kok(81)

# ================================================================================================================================================
# 9 - Girilen paremetrenin logaritmasını alan fonksiyon yazdırın.

def log_al(num):

    num = math.log(num)

    print(num)
log_al(100000)

# ================================================================================================================================================
# 10 - Girilen parametrelere göre dik üçgenin hipnotenüsünü bulan fonksiyon yazın.
def dik_ucgen(a,b):

    hip = math.sqrt(a**2+b**2)
    print(hip)
dik_ucgen(20,30)
