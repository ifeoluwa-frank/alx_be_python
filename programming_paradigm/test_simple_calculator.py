from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(-10, 5), -15)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            SimpleCalculator.divide(self, 10, 0)

if __name__ == "__main__":
  unittest.main()
