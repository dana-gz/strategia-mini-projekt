from wojownik import Wojownik


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__(60)


    def attack(self):
        print('Rycerz: Machnąłem mieczem!')
        self._exp += 0.3
