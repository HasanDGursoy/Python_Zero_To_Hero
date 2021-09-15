"""
import <modul_adi>

Python Modulleri 3 şekilde arar:
1-Bu kodun çalıştığı klasörlerde arar (aynı seviyede)
2-PYTHONPATH environment variable --> tanımlı
3-Python'un kurulu olduğu klasörlerde arar (kendi klasörlerdr virtul env'lerde)

sys.path --> arama klasörlerini gösterir
"""

# Searc Path'i görelim

import sys

sys.path

python_search_path = sys.path
print(python_search_path)

# tek tek yazdıralım
for path in python_search_path:
    print(path)

# örnek :
# moduller\girdi

import moduller.girdi_islemleri_modul as girdi

metin = girdi.tam_sayi_al()
print(metin)

"""
Klasör yolu ile modullere erişim doğru bir yol değildir --> Çünkü klasör adı değişebilir.
"""

"""
Lokal Erişim : python101\venv\lib\site-packages
"""
# Örnek : Local erişimden ulabilmek için local erişim adresine modulumuzu koymak yeterli .

"""
Bu makine üzerinde bütün python kodlarının erişebileceği yapı : 
Global Erişim : \Python\Python39\lib 
yani python library klasöründe
Module ulaşmak için lib'e modulumuzu yukleyebiliriz.
"""

