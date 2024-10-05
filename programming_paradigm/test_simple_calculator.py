from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition_positive(self):
        result = SimpleCalculator.add(self, 5, 3)
        self.assertEqual(result, 8)

    def test_add_negative(self):
        result = SimpleCalculator.add(self, -2, 7)
        self.assertEqual(result, 5)

    def test_sub_positive(self):
        result = SimpleCalculator.subtract(self, 10, 5)
        self.assertEqual(result, 5)

    def test_sub_negative(self):
        result = SimpleCalculator.subtract(self, -5, 5)
        self.assertEqual(result, -10)

    def test_multiply(self):
        result = SimpleCalculator.multiply(self, 5, 3)
        self.assertEqual(result, 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            SimpleCalculator.divide(10, 0)

if __name__ == "__main__":
  unittest.main()
