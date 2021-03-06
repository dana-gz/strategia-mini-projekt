import unittest
from wojownik import Wojownik, LifeError
from jednostki.rycerz import Rycerz


class TestWojownik(unittest.TestCase):

    def test_warrior_alive(self):
        war = Wojownik(30)
        self.assertEqual(war._hp, 30)
        self.assertEqual(war._exp, 0)

    def test_warrior_with_incorrect_life_value(self):
        with self.assertRaises(LifeError):
            Wojownik(-100)

    def test_repr(self):
        war = Wojownik(30)
        expected = 'Wojownik - życie = 30, doświadczenie = 0'
        received = war.__repr__()
        self.assertEqual(expected, received)

    def test_march(self):
        expected = 1000 * 0.02
        war = Wojownik(30)
        war.march(1000)
        self.assertEqual(expected, war._exp)


class TestRycerz(unittest.TestCase):

    def test_knight_parametrers(self):
        ry = Rycerz()
        self.assertEqual(ry._hp, 60)
        self.assertEqual(ry._exp, 0)

    def test_knight_attack(self):
        ry = Rycerz()
        ry.attack()
        self.assertEqual(0.3, ry._exp)


if __name__ == '__main__':
    unittest.main()
