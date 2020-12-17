import unittest
from test import calc


class TestProgression(unittest.TestCase):
    test = calc(2.56)

    def test_add__(self):
        self.assertEqual(self.test.__add__(3), 5.5600000000000005)
        self.assertEqual(self.test.__add__(2.44), 5)
        self.assertTrue(self.test.__add__(487), isinstance(self.test.__add__(487), float))

    def test_sub__(self):
        self.assertEqual(self.test.__sub__(2), 0.56)
        self.assertEqual(self.test.__sub__(1), 1.56)

    def test_mul__(self):
        self.assertEqual(self.test.__mul__(2), 5.12)
        self.assertEqual(self.test.__mul__(4), 10.24)


if __name__ == '__main__':
    unittest.main()
