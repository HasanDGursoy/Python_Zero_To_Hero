# METİN KARŞILAŞTIRMA

meyve = "armut"
elma = "elma"
armut = "armut"
if meyve == "armut":
    print("evet armut")
else:
    print("armut değildir.")

if armut < elma:
    print("{0}, {1} 'dan küçüktür. ".format(armut, elma))
else:
    print("{0}, {1} ' den küçüktür. ".format(armut, elma))

# bunun cevabı armut elmadan küçükdür. Peki Neden ?
# armut 'a' ile başladığı için elmanın 'e' sinden önce geliyor işte bu yüzden.
# Bu duruma ASCII (American Standard Code for Information Interchange) sayesinde karar veriyolar.
# ASCII karakterlerini görmek için -> ord() fonksiyonu kullanılır.

print(ord('a'))
print(ord('A'))
print(ord('e'))
print(ord('E'))

# ASCII de büyük harfler küçük harflerden önce gelir. İnsan algısının tersidir yani

print('A' > 'a')  # false çıkacak
print('z' > 'Z')  # True çıkacak
