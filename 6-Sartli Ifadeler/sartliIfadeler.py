# Şartlı ifadeler if-else ifadelerini göreceğiz
# Şartlı ifadeler mantıksal operatorler ile kontrol edilir.

# eşitlik kontrol -> ==
a = 6
print(a == 8)
print(type(True))

a = True
b = False

print("{0} and {1} : {2}".format(a, b, a and b))

if 0 < a < 10:
    print("selam")

name = "hasan"
tip = "yakışıklı"

if name == "hasan" and tip == "yakışıklı":
    print("Hasan Fena Birşeydir.")
else:
    print("Hasan Her halükarda yakışıklıdır.")


def haftanin_gunleri():
    gun_adi = ""
    # Kullanıcıdan bir gün numarası isteyelim
    # Direk aldığımız değeri int olarak çeviremeyiz.(cast edemeyiz)
    # Önce girdi kontrol etmemiz lazım
    girdi = input("Lütfen Bir gün numarası giriniz : ")

    # Konrol 1 : Tam sayı kontrolü
    # Girdinin tam sayı olmasını isitiyoruz.
    # O zaman int kontrolü yapmamız lazım --> isdigit() fonksiyonu ile

    if girdi.isdigit():
        gun_numarasi = int(girdi)
    else:
        print("Lütfen Tam Sayı Giriniz !")
        return
    print("---------------- 1. Kontrol Başarılı ---------------")

    # Konrol 2 : Sayının 1-7 arasında olma kontrolü
    # Bu noktaya gelmişsek -> 1.Kontrol başarılıdır ve gün numarasına sıra gelmiştir.

    if gun_numarasi < 1 or gun_numarasi > 7:
        print("Lütfen 1 - 7 arasında bir sayı giriniz.")
        return

    print("---------------- 2. Kontrol Başarılı ---------------")

    if gun_numarasi == 1:
        gun_adi = "PAZARTESİ"
    elif gun_numarasi == 2:
        gun_adi = "SALI"
    elif gun_numarasi == 3:
        gun_adi = "ÇARSAMBA"
    elif gun_numarasi == 4:
        gun_adi = "PERŞEMBE"
    elif gun_numarasi == 5:
        gun_adi = "CUMA"
    elif gun_numarasi == 6:
        gun_adi = "CUMARTESİ"
    else:
        gun_adi = "PAZAR"

    print("Bu gün : " + gun_adi + " günüdür.")


haftanin_gunleri()

# İç İçe geçmiş if-else yapısı

girdi = input("1-10 arasında bir sayı giriniz : ")

if girdi.isdigit():
    sayi = int(girdi)

    if sayi <= 10:
        if sayi % 2 == 0:
            print("Girdiğiniz sayi çifttir.")
        else:
            print("Girdiğiniz sayi tektir.")

    else:
        print("Lütfen 1- 10 arasında bir sayı giriniz !!!")

if not 5 == 5:
    print("selamlar")
else:
    print("Merhabalar")