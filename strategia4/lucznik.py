from wojownik import Wojownik


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
