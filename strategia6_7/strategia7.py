from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik

rycerze = []
for i in range(4):
    rycerze.append(Rycerz())

print(rycerze)

for rycerz in rycerze:
    rycerz.march(2000)

rycerze.append(Rycerz())

for rycerz in rycerze:
    rycerz.attack()

print(rycerze)


lucznicy = []
for i in range(3):
    lucznicy.append(Lucznik())

print(lucznicy)

armia = rycerze + lucznicy
for wojownik in armia:
    wojownik.attack()

print(armia)