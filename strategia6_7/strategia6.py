from jednostki.rycerz import Rycerz



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

