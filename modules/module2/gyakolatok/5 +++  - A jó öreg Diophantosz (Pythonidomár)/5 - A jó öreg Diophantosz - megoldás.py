"""
Előtanulmány: oldjuk meg az x2 + 2x + 5 = 11668 egyenletet a természetes számok halmazán… Nem, nem, csak semmi megoldóképlet,
mert attól a phalra mászunk. Majd próbálgatunk, jó??

Adott az egyenlet:
    a, talald meg ciklus segitsegevel a pozitiv gyökét
    b, találd meg a negatív gyökét
"""

x = 0
while x**2 + x*2 + 5 != 11668:
    x += 1
print(x, 'a megoldás.')
