"""
Klasor Yaratma
:
1- os.mkdir()
  * mkdir() -> tek klasör yaratır
  * makedirs() -> birden fazla klasör yaratıyor

2- path.Path.mkdir() -> hem tekli hem de çoklu klasor yaratır.
"""

# ana klasör yolu
import os
import pathlib

dosya_yolu = os.getcwd()

# örnek:

# 1.yol os.mkdir()
# dosya zaten var -> FileExistsError bu hatayı alırız eğer varsa

# os.mkdir('ornek_klasor_1')
# os.mkdir('ornek_klasor_2')

# 2. yol -> pathlib.Path.mkdir()

# pathlib.Path('path_klasor_1').mkdir()
#
# try:
#     pathlib.Path('path_klasor_1')
# except:
#     print('Klasor zaten var yada baska bir hata yaptınız')
#


# BİRDEN FAZLA DOSYA KLASOR OLUSTURMA

"""
- seviye 1
    - seviye 2
        - seviye 3
"""

# 1. yol - > os.makedirs()

os.makedirs('seviye_1/seviye_2/seviye_3', exist_ok=True)  # exist_ok=True varsa kızma demek hata dan korur.

# 2. yol - > pathlib.Path.mkdir()

p3 = pathlib.Path('path_seviye_1/path_seviye_2/path_seviye_3')
p3.mkdir(parents=True,exist_ok=True)  # parents=True eğer ilk klasör yoksa ebeveyn oluştur demekdir.)
