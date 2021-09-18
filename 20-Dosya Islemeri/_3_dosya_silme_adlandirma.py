"""
Python'da dosyaları :
* yeniden adlandirma (rename)
* silme
* yaratma

os modulu ile yapılır
"""
import os

# YENİDEN ADLANDİRMA --> rename()
# örnek


# os.rename('silinecek.txt', 'silinmeden_once_rename.txt')

# dosya yoksa hata alırız. bu yüzden try cath de yaparız sorun ortadan kalkar

# SİLME --> remove(), unlink()

# os.remove('silinmeden_once_rename.txt')
# os.unlink('silinecek.txt')


# YARATMA --> open(......, mode='x')

# with open('silinecek.txt', mode='x', encoding='utf-8') as dosya:
#    dosya.write('Bu dosya open(mode = "x") ile yaratıldı.')


"""
Encoding : 
cp1254 --> Windows'un Türkçe Encoding Formatı

OS encodingleri ile uğraşmamak için --> open() işlemlerinde encdoing = 'utf-8'
"""
