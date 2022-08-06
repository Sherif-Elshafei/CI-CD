import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(3),pi*3**2)

    def test_value(self):
        self.assertRaises(ValueError,circle_area,-1)

    def test_type(self):
        self.assertRaises(TypeError,circle_area,"circle")

    #TestCircleArea.test_area()
#if __name__ == '__main__':
 #   unittest.main()
