"""
iki yol :

* String metodları --> startswith, endswith, find
* fnmatch modulu
"""

# Örnek
# String Metodları

# Arama klasoru
# stringlerin başına '\' işareti varsa --> r harfi koyarsak raw string anlamına gelir.
import os
from pathlib import Path
import fnmatch

arama_klasoru = r'C:\Windows'

# önce bu dizinin içini görelim
# for k in os.listdir(arama_klasoru):
#     print(k)

# şimdi .exe olan dosyaları bulalım

# with Path(arama_klasoru) as klasor:
#     # klasor içindeki nesneler
#     for i in klasor.iterdir():
#         # type file mi bakıcaz ve .exe
#         if i.is_file() and i.name.endswith('.exe'):
#             print(i.name)


# fnmatch modulu ile yapalım
# önerilen yöntem

desen = '*.exe'
with Path(arama_klasoru) as klasor:
    for dosya in klasor.iterdir():
        if dosya.is_file() and fnmatch.fnmatch(dosya.name, desen):
            print(dosya.name)
