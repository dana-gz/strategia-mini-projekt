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