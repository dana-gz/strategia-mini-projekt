from jednostki.wojownik import Wojownik


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self._hp = 60

    def attack(self):
        print('Rycerz: Machnąłem mieczem!')
        self._exp += 0.3
