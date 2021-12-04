import unittest
from description import compare, shape,size
from calculation.rectangle_cal import Rectangle
from calculation.round_cal import Round


class TestCompare(unittest.TestCase):
    def test_is_same_shape(self):
        a = Round(5)
        b = Round(6)
        c = Rectangle(1,1)
        self.assertEqual(compare.is_same_shape(a,b),True)
        self.assertEqual(compare.is_same_shape(a,c),False)
    def test_is_same(self):
        d = Round(5)
        e = Round(5)
        f = Rectangle(2,6)
        self.assertEqual(compare.is_same(d,e),True)
        self.assertEqual(compare.is_same(d,f),False)
    def test_big_area(self):
        g = Round(5)
        h = Round(6)
        i = Rectangle(6,170)
        self.assertEqual(compare.big_area(g,h),h)
        self.assertEqual(compare.big_area(g,i),i)
unittest.main(argv=[''],verbosity=2,exit=False)
