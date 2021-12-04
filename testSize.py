import unittest
from description import compare, shape,size
from calculation.rectangle_cal import Rectangle
from calculation.round_cal import Round
class TestSize(unittest.TestCase):
    def test_change_side_for_rec(self):
        a = Rectangle(3,5)
        self.assertEqual(size.change_side_for_rec(a,"long",3).long_len,8)
    def test_change_radius_for_round(self):
        b = Round(5)
        self.assertEqual(size.change_radius_for_round(b,3).radius,8)
    def test_change_area(self):
        c = Rectangle(2,3)
        self.assertEqual(size.change_area(c,4).area,10)
unittest.main(argv=[''],verbosity=2,exit=False)
