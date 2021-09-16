"""
3. f-strings(string interpolation)
* f-strings python 3 ile geldi (yeni)
* f'........string.........'
* str.format() gibi çalışır ama daha dinamikdir.
* {} süslü parantezler ile kullanılır.
"""
y = 2
x = 3

carpim = x * y
print(f'{x} * {y} = {carpim}')

# direk {} parantez içinde işlem yapılabilir.

veri = ['Klark Kent', 'Metropolis', 'Daily Planet']
print(f'{veri[0]}, yani superman, kurgusal {veri[1]}, şehrinde {veri[2]} gazetesinde çalışır')

# Onemli Not:
# f-strings Python 3.6 ile geldi daha alt bir versiyonda kullanılmaz.
