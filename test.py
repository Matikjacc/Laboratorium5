import unittest
from main import npt,Point

class testnpt(unittest.TestCase):
    def test_npt_1(self):
        dane = []
        dane.append(Point(0,-2))
        dane.append(Point(-3, 1))
        dane.append(Point(2, 6))
        actual = npt(dane)
        self.assertEqual(npt(dane), True)

    def test_npt_2(self):
        dane = []
        dane.append(Point(0,-2))
        dane.append(Point(-1,-5))
        dane.append(Point(2, 7))
        dane.append(Point(7, -7))
        actual = npt(dane)
        self.assertEqual(npt(dane), False)

    def test_npt_3(self):
        dane = []
        dane.append(Point(-4,0))
        dane.append(Point(4, 5))
        dane.append(Point(9, -3))
        actual = npt(dane)
        self.assertEqual(npt(dane), True)

    def test_npt_4(self):
        dane = []
        dane.append(Point(8,2))
        dane.append(Point(12, 2))
        dane.append(Point(12, 8))
        actual = npt(dane)
        self.assertEqual(npt(dane), False)


if __name__ == '__main__':
    unittest.main()
