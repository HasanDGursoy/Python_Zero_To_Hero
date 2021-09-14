"""
Şimdiye kadar şunları gördük

    try:
        <--- kod --->
    except:
        <--- hata --->
    else:
        <--- hatasız işlem --->
    finally:
        <--- ne olursa olsun çalış --->
"""


# Örnek:

def bolme(x, y):
    try:
        result = x / y

    except ZeroDivisionError as ex:
        print(ex)
    else:
        print('Sonuc : ', result)
    finally:
        print('İşlem tamamlandı.')


# hatalı çağırma
bolme(5, 0)

# dogru çağırma
bolme(5, 5)


# örnek
def dosya_open(path):
    try:
        file = open(path)
    except Exception as ext:
        print(ext)
    else:
        print(file.read())
    finally:
        try:
            file.close()
        except:
            pass # hiç birşey yapma

dosya_open('ornek.txt')

# Yukarıdaki dosya_open fonksiyonundaki olay dosya adı yanlış girilirse finally de yani her ne olursa olsun
# çalıştır kısmında ilk başta olmayan bir dosyayı kapatmaya çalıştık pyhonda halilye error verdi o kısmıda kendi kod
# bloğunda try except mantığı kurunca ordaki hata alma olayınıda ortadan kaldırıyoruz.