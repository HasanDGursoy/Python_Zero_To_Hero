"""
ARŞİV DOSYASI AÇMA İŞLEMİ
zipfile ile yapılır
"""
import zipfile
import os
import shutil

# for d in os.listdir():
#     print(d)
#
# # hadi bu arsiv.zip dosyasını açalım
#
# arsiv = zipfile.ZipFile('arsiv.zip', mode='r')
# print(arsiv)
#
# # extract etmeden önce, içinde ne var bakalım
# # süpriz :S
# for i in arsiv.filelist:
#     print(i.filename)
#
# # şimdi extract edelim
# arsiv.extractall()
#
# # arsiv'i kapat
# arsiv.close()

# ARŞİV DOSYASI YARATMA
# shutil.make_archive()

shutil.make_archive('yeni_arsiv', 'zip', 'arsiv')
