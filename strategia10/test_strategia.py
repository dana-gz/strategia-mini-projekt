import unittest
from wojownik import Wojownik, LifeError

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
        expected = 'Wojownik: zycie=30, doswiadczenie=0'
        received = war.__repr__()

        self.assertEqual(expected, received)


if __name__ == '__main__':
    unittest.main()
