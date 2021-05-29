class Knight:
    def __init__(self):
        self.hp = 60
        self.exp = 0

    def __repr__(self):
        return f'Rycerz: życie:{self.hp}, doświadczenie:{self.exp}'

    def march(self, distance):
        self.exp += distance * 0.2
        print(f'Rycerz: Przeszedłem {distance}m.')
        return self.exp

    def atack(self):
        self.exp += 0.3
        print('Rycerz: Machnąłem mieczem!')
        return self.exp


class Archer:
    def __init__(self):
        self.hp = 40
        self.exp = 0
        self.arr = 100

    def __repr__(self):
        return f'Łucznik: życie:{self.hp}, doświadczenie:{self.exp}'

    def march(self, distance):
        self.exp += distance * 0.02
        print(f'Łucznik: Przeszedłem {distance}m.')
        return self.exp

    def atack(self):
        if self.arr > 0:
            self.exp += 0.4
            self.arr -= 1
            print('Łucznik: Wypuściłem strzałę!')
            return self.exp
        else:
            print('Lucznik: Nie mam już strzał.')


if __name__ == '__main__':

    ge = Knight()
    ge.hp = 50
    ge.exp = 10
    print(ge)
    ge.march(1000)
    ge.atack()
    print(ge)

    pi = Archer()
    print(pi)
    pi.march(200)
    pi.atack()
    print(pi)
