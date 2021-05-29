from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik


class Druzyna:
    def __init__(self):
        self.wojownicy = []

    def dodaj_wojownika(self, wojownik):
        self.wojownicy.append(wojownik)

    def march(self, distance):
        for woj in self.wojownicy:
            woj.march(distance)

    def attack(self):
        for woj in self.wojownicy:
            woj.attack()

    def raport(self):
        together = len(self.wojownicy)
        print('W drużynie jest {} wojowników:'.format(together))
        for woj in self.wojownicy:
            print(woj)


def main():
    ry = Rycerz()
    print(ry)
    troop = Druzyna()
    troop.wojownicy.append(ry)
    lu = Lucznik()

    troop.wojownicy.append(lu)
    print('---------------------------------')
    troop.march(1000)
    print('---------------------------------')
    troop.attack()
    print('---------------------------------')
    troop.raport()
    print('---------------------------------')


if __name__ == '__main__':
    main()
