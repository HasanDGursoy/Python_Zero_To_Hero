# FONKSİYON DÖNEN FONKSİYON

def katini_al(n):
    """

    :param n: int
    :return: lambda a : a * n şeklinde bir lambda fonksiyon
    """
    return lambda a : a *n

ikili_katlar = katini_al(2)
value = ikili_katlar(10)
uclu_katlar = katini_al(3)
value1 = uclu_katlar(10)

print(value)
print(value1)
