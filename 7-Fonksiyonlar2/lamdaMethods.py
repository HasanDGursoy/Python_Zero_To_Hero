# LAMBDA FONKSİYONU : lambda

# Bazen, bir fonksiyonu isim vermeden direk kullanmak isteyebiliriz.
# lambda fonksiyonu (lambda expression) tek satır fonksiyonu olarak da bilinir.
# örn.

metin = "Selam Sana Kartal Gözü"
print(metin.split())

# Şimdi bir labda fonksiyonu ile split() fonksiyonu kullanalım

metni_parcala = lambda x: x.split()  # bir fonksiyon :D
print(metni_parcala(metin))

# Çarpma yapan lambda fonksiyonu tanımlayalım

multiply = lambda x, y: x * y
carpma = multiply(10,20)
print("Çarpım : ",carpma)

# Üstel hesaplama yapan bir lambda fonksiyon
ustel = lambda sayi ,ust : sayi **ust
ust_hesapla = ustel(10,30)
print(ust_hesapla)
