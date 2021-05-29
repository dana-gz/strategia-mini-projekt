class Wojownik:
    def __init__(self):
        self._exp = 0

    def __repr__(self):
        part = self.__class__.__name__
        return f'{part} - życie = {self._hp}, doświadczenie = {self._exp}'

    def march(self, distance):
        part = self.__class__.__name__
        self._exp += distance * 0.02
        print(f'{part}: Przeszedłem {distance}m.')


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self._hp = 60

    def attack(self):
        print('Rycerz: Machnąłem mieczem!')
        self._exp += 0.3


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self._hp = 40
        self._arr = 100

    def attack(self):
        if self._arr > 0:
            self._exp += 0.4
            self._arr -= 1
            print(f'Lucznik: Wypuściłem strzałę!  Zostały mi jeszcze {self._arr} strzały.')
            return self._exp
        else:
            print('Lucznik: Nie mam już strzał.')


def main():
    ge = Rycerz()
    print(ge)
    ge.march(1000)
    ge.attack()
    print(ge)

    lu = Lucznik()
    print(lu)
    lu.march(15)
    print(lu)
    lu.attack()
    print(lu)


if __name__ == '__main__':
    main()
