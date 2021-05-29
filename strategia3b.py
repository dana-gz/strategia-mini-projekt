class Warrior:
    def __repr__(self):
        part = self.__class__.__name__
        return f'{part} - życie: {self._hp}, doświadczenie:{self._exp}'

    def march(self, distance):
        part = self.__class__.__name__
        self._exp += distance * 0.02
        print(f'{part}: Przeszedłem {distance}m.')


class Knight(Warrior):
    def __init__(self):
        self._hp = 60
        self._exp = 0

    def attack(self):
        self._exp += 0.3
        print('Rycerz: Machnąłem mieczem!')
        return self._exp


class Archer(Warrior):
    def __init__(self):
        self._hp = 40
        self._exp = 0
        self._arr = 100

    def attack(self):
        if self._arr > 0:
            self._exp += 0.4
            self._arr -= 1
            print(f'Łucznik: Wypuściłem strzałę!  Zostały mi jeszcze {self._arr} strzały.')
            return self._exp
        else:
            print('Łucznik: Nie mam już strzał.')


def main():
    ge = Knight()
    print(ge)
    ge.march(1000)
    ge.attack()
    print(ge)

    pi = Archer()
    print(pi)
    pi.march(200)
    pi.attack()
    print(pi)


if __name__ == '__main__':
    main()
