"""
Bir klasör içindeki tüm dosya ve klasörleri os modülü ile okuruz.
Bunların tipi:
 * dosya
 * klasör
"""

# --------- Tüm klasör içeriğini okuma --------- #

# 1.Yol --> os.listdir()
import os

# okunacak klasör ->
dosya_yolu = os.getcwd()

# icerik = os.listdir(dosya_yolu)
# print(icerik)
#
# for ic in icerik:
#     print(ic)

# 2. Yol --> os.scandir()

folder = os.scandir(dosya_yolu)

# for eleman in folder:
#     print(eleman)

# 3. Yol --> pathlib.Path

import pathlib

# icerik = pathlib.Path(dosya_yolu).iterdir()
# for ic_eleman in icerik:  # objenin elemanlarını iterdir() olarak almassak hata alırız.
#     print(ic_eleman)

# print()
# print("------------------------------------------")
# print()
# ----------- Klasör İçerisindeki Dosyaları Okuma ------------ #

# 1.Yol --> os.listdir()

# icerik = os.listdir(dosya_yolu)
# for ic in icerik:
#     if os.path.isfile(ic):
#         print(ic)

# 2.Yol --> os.scandir()
# with os.scandir(dosya_yolu) as scans:
#     for scan in scans:
#         if scan.is_file():
#             print(scan)

# 3. Yol --> pathlib.Path.iterdir()

# ana_dosya = pathlib.Path(dosya_yolu).iterdir()
#
# for dos in ana_dosya:
#     if dos.is_file():
#         print(dos)

# ----------------- Klasör İçindeki Klasörleri Okuma ----------------- #

# os.listdir()
icerik = os.listdir(dosya_yolu)
for i in icerik:
    if os.path.isdir(i):
        print(i)

# os.scandir()

icerik = os.scandir(dosya_yolu)
for a in icerik:
    if a.is_dir():
        print(a)

# patlib.Path().iterdir()

dosya = pathlib.Path(dosya_yolu).iterdir()
for e in dosya:
    if e.is_dir():
        print(e)