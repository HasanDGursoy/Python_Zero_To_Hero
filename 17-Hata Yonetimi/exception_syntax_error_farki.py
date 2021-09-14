"""
1- Exception ile syntax error farkı :

Bir python programı, bir hata ile karşılaştığında durur.
İşte, bu duruma işleminin nasıl olacağına Exception Handling denir.(Hata Yönetimi)

Python'da hata iki türlü olur.
 1-Syntax Error (Yazım Hatası)
 2-Exception Error (Uygulama Hatası)


"""
"""
Syntax Error (Sözdizimi Hatası):

Python Parser'ı (kod oluşturucu) yazım şekli Python kurallarına uymuyorsa, 'Syntax ERROR ' üretir.
Hata Tipi : SyntaxError
Parantez koymayı unutursunuz, çift tırnakla başlayıp tek tırnakla değer oluşturursunuz yada tam tersini
yaparsınız, fonksiyon, if bloğu , döngü oluştururken ':' koymayı unutsunuz vs bunun gibi şeyler.

"""
"""
Exception Error : Syntax'ı doğru olan, ama Python Interpreter'ın çalışırken  (run-time) aldığı hatalardır.

Örnek : a = 7 / 0 
Yediyi sıfıra bölmeğe çalışırsak böyle bir şey olmadığı için hata alırız.

Örnek : print(t)
T diye bir değişken tanımlamadığımız halde yazdırmaya çalışıyoruz.

Bunun gibi hatalar Exception Hatalardır.


"""

