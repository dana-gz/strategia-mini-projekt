from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik
from wojownik import Wojownik


class Druzyna:
    def __init__(self):
        self.wojownicy = []

    def dodaj_wojownika(self, wojownik):
        self.wojownicy.append(wojownik)

    def march(self, distance):
        for woj in self.wojownicy:
            woj.march(distance)


def main():
    ry = Rycerz()
    print(ry)
    troop = Druzyna()

    troop.wojownicy.append(ry)

    lu = Lucznik()

    troop.wojownicy.append(lu)

    troop.march(1000)


if __name__ == '__main__':
    main()
