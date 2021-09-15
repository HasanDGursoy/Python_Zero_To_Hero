"""
Standart Modüller

"""
import os

"""
Moduler Programlama:
1-Kod Tekrarını önler
2-Organizasyon (web,db,api...)
3-Bakım ve yönetimi kolaylaştırır
"""

"""
Modul: .py ile biten Python dosyalarına biz modul diyoruz.
Paket: Birçok modulu içeren Python klasörleridir.
"""

"""
Moduller 'import' edilerek kullanılır
"""
import math

# pi sayısı
pi_sayisi = math.pi
print(pi_sayisi)

# import --> Python Interpreter sizin için o dosyayı buraya getirir.

# Örnek
# random

import random

# random.random() -> 0 ile 1 arasında olasılık veriir
olasilik = random.random()
print(olasilik)

# 10 ile 50 arasında rastgele
rastgele_sayi = random.randint(10, 50)
print(rastgele_sayi)

# listeden rastgele eleman almak
liste = [1, 2, 3, 4, 5, 6]
eleman = random.choice(liste)
print(eleman)

# orneklem almak için
orneklem = random.sample(liste, 3)
print(orneklem)

"""
platform modülü
"""

import platform

print('Platform : ', platform)

# platform türü
print('Platform Türü : ', platform.platform())

# platform mimarisi
print('Platform Mimarisi : ', platform.architecture())

# makine tipi
print('makine tipi : ', platform.machine())

# os
print('İşletim sistemi : ', platform.system())

"""
sys modulu
"""

import sys

# path değişkeni
# print('path : ',sys.path)

yollar = sys.path

for yol in yollar:
    print(yol)

# sys.path --> Python'un modul ararken kullandigi yollar

"""
bir modul import ederken adını değiştirmek isteyebiliriz
alise = yeniden adlandırma
"""

import random as rnd

print(rnd.random())

"""
Tek seferdebirden fazla import
import a,b,c
"""
import random, sys, os

"""
Bir modulun bir parçasını import etmek

from <modul_adi> import <modul_parcasi>

"""
from sys import modules

print('Hazır moduller', modules)

# hem parçalı hem de alise edilmiş import
from math import sqrt as karakok

print('4 ün  karakökü', karakok(4))

"""
* ile import  = ancak bu tavsiye edilmez isim karmaşası yaşatır "import * " önerilmez.
from random import * 
"""

