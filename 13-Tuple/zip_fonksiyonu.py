# ZİP() FONKSİYONU
# Pythonda list ve tuple tipleri beraber kullanıldıklarında çok işlevsel olurlar.Bunu detaylı görmek için önce zip() fonksiyonunu görelim
# İki veya daha fazla dizi (index ile erişilebilen tipler: List,tuple,string,range) tipinde değişken alır.
# zip yani fermuar fonksiyonu adından da anlaşılabileceği gibi her bir dizideki karşılıklı elemanları alarak bir tuple oluşturur. Böylece tuple'lardan oluşan bir zip nesnesi döner.

metin = 'xyzt'
liste = [1, 2, 3, 4]

# metin ve listeyi zipleyelim

fermuar = zip(metin, liste)
print(fermuar)

for i in fermuar:
    print(i)

# fermuarı döngüyle gezebiliyoruz ancak index değerlerine teker teker ulaşamıyoruz.

# Eğer zip nesnesini list olarak almak istiyorsak --> list() yazmamız yeterlş

fermuar = list(fermuar)
print(fermuar)

# yazdırdık ama boş liste oldu çünkü fermuar sonuna kadar gitmişti for döngüsünde tek kullanımlık peçete gibi eğer bunu yapmassa sonsuz döngüye girer.
# İteratörler sadece 1 kere çalışır.

d1 = ['A', 'B', 'C', 'D', 'E']
d2 = [10, 20, 30]

yeni_fermuar = zip(d1, d2)

# yeni_fermuar değişken hiç okumadan listeye çevirelim

yeni_fermuar = list(yeni_fermuar)
print(yeni_fermuar)

for a in yeni_fermuar:
    print(a)

for d1_eleman, d2_eleman in yeni_fermuar:
    print("d1'den gelen : {0} , d2'den gelen : {1}".format(d1_eleman, d2_eleman))

# Alıştırma :
# Verilen iki listedeki karşılıklı elemanları kontrol edelim
# ikiside eşitse yazdıralım

l1 = ["a", "B", "C", "d", "e", "F"]
l2 = ["A", 'B', "c", 'd', 'E', "F"]

for e1,e2 in zip(l1,l2):

    if e1 ==e2:
        print(e1)
