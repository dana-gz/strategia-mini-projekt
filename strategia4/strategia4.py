from rycerz import Rycerz
from lucznik import Lucznik


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
