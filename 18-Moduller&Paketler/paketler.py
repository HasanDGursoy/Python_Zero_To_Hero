"""
Python Paketleri -> aslında birer klasördür
* tek farkı -> içinde __init__.py adında bir python dosyası vardır.

Paketler:
* kodu organize ederler
* paketler taşınabilirdir.
* modulleri birleştirir.

Paket altındaki module erişmek:
* pak1.mod1
* pak2.mod2.mod21...
"""

"""
Paket Yaratmak
    *__init__.py -> içinde, alt paketler ve moduller için importlar
    * global değişkenler 
    * dokumantasyonlar
"""

# ------------------------- pak paketini import edelim ----------------------------------
# sadece pak 'ı import ederek içindekileri import edemeyiz.
# pak'ın içindeki init'e modulleri import edip direk burdaki kısımda paketi çağırırsak 'absolute import' hatası alırız.
# biz relative import yapmak zorundayız.
# yani global gibi değil olduğumuz yerde ver dicez. Tabi ki __init__ dosyasında yapıcaz.

# paketin altındaki modul ->
import pak

pak.mod_2.print_mod_2()
pak.mod_1.print_mod_1()

