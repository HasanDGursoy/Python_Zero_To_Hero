# Stringler İmmutable sa nasıl değişim sağlayacağız.
# Bunu işlicez.

selamla = "hello world"

print(selamla[:6])
print(selamla[7:])

selamla = selamla[:6] + "W" + selamla[7:]
print(selamla)