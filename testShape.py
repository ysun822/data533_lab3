import unittest
from description import compare, shape,size
from calculation.rectangle_cal import Rectangle
from calculation.round_cal import Round


class TestShape(unittest.TestCase):
    def test_round_to_square(self):
        a = Round(5)
        self.assertEqual(type(shape.round_to_square(a)),Rectangle)
    def test_square_to_round(self):
        b = Rectangle(3,3)
        self.assertEqual(type(shape.square_to_round(b)),Round)
    def test_round_to_rect(self):
        c = Round(5)
        self.assertEqual(type(shape.round_to_rect(c,2)),Rectangle)
unittest.main(argv=[''],verbosity=2,exit=False)
