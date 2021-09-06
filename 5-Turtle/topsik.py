import turtle


# Yeri gelmişken yazayım eğer dosya ismi yada python sayfasının ismi import edilmeye çalışılanşeyle aynıysa oluşturdugumuz dosya import edilir.
# Python da hazır olarak gelen bir modüldür "turtle"
# Şimdi kaplumbağa yaratan bir fonksiyon yazalım.

def kaplumbaga_yarat():
    # Turtle nesnesi yarat
    tospik = turtle.Turtle()

    print(tospik)
    return tospik


## mainloop fonksiyonu açılan pencereye kullanıcının herhangi bir işlem yapana kadar beklemesini söyler.
# mainloop fonksiyonu her zaman kodun en sonunda olmak zorunda .


"""
Method == Fonksiyon

# KAPLUMBAGA 

turtle.fd(n) --> n pixel kadar ileri hareket ettirir.
turtle.bk(n) --> n pixel kadar geri hareket ettirir.
turtle.lt(d) --> d açısı kadar sola döner. 
tutle.rt(d) --> d açısı kadar sağa döner.
"""

# kamplumbaga al
t = kaplumbaga_yarat()
# kaplumbagıyı hareket ettir.
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
#-- altına bir tane daha kare yapıcam :D
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(200)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)

turtle.mainloop()
