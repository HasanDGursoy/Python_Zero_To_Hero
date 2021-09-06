# Fonksiyonlar geriye bir değer döndürebilir bunu "return" ile sağlıyoruz.
# Fonksiyon geriye değer dönmüyorsa void'tir.

def cube(n):
    n_kup = n ** 3
    return n_kup


# bu fonksiyonun değerini alıp bir değişkene atayabiliriz.

kup = cube(10)
print(kup)

user_name = "user"
user_pass = 123


def user_login(name, user_pass):
    a = name
    b = str(user_pass)

    return a + " " + b

user = user_login(user_name,user_pass)
print(user)

