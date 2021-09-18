"""
1- Klasor Silme
2- Dosya ve Klasor Kopyalama
3- Dosya ve Klasor Taşıma
4- Klasoru Yeniden Adlandırma
"""

import shutil
import os
import pathlib

# 1- KLASOR SİLME
"""
* os.rmdir() --> tek klasor siler (klasör boş olması lazım yoksa silmez)
* pathlib.Path.rmdir() --> tek klasor siler (klasor Boş ise siler)
* shutil.rmtree() --> tüm klasör ağacını siler 
"""

# önce silinecek klasör yarat
# os.mkdir('klasor_silinecek')

# silinecek_klasor boş olduğu için --> os.rmdir() bunu silebilir
# os.rmdir('klasor_silinecek')

# dolu klasor silmeyi --> shutil
# shutil.rmtree('klasor_silinecek')

# 2- DOSYA VE KLASOR KOPYALAMA
# Dosya Kopyalama
# shutil.copy()
# shutil.copy2()
# Source --> Destination

# src = 'kaynak_klasor/k1.txt'
# dst = 'hedef_klasor/h1.txt'
#
# shutil.copy2(src, dst)

# KLASOR KOPYALAMA
# shutil.copytree()
# shutil.copytree('kaynak_klasor','kaynak_klasor_kopyasi')

# 3 - DOSYA VE KLASOR TASIMA
# shutil.move(kaynak,hedef)
# shutil.move('kaynak_klasor/k1.txt','hedef_klasor')
# shutil.move('kaynak_klasor_kopyasi', 'hedef_klasor')


# 4 - KLASOR YENİDEN ADLANDIRMA
# os.rename('kaynak_klasor', 'final_klasor')

