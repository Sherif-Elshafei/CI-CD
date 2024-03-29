import unittest
from circles2 import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
        def test_area(self):
                #test area when r>=0
                self.assertAlmostEqual(circle_area(1), pi)
                self.assertAlmostEqual(circle_area(0), 0)
                self.assertAlmostEqual(circle_area(2.1), pi*(2.1**2))
        def test_value(self):
                #make sure value errors are raised when necessary
                self.assertRaises(ValueError, circle_area, -2)

        def test_types(self):
                #make sure type errors are raised when necessary
                self.assertRaises(TypeError, circle_area, 3+5j)
                self.assertRaises(TypeError, circle_area, True)
                self.assertRaises(TypeError, circle_area, "circle")

if __name__ == '__main__':
        unittest.test_circles2()
