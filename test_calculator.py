import unittest
from calculator import add, multiply

class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_mixed_signs(self):
        self.assertEqual(add(-2, 3), 1)

    def test_zero(self):
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_mixed_signs(self):
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)

    def test_zero(self):
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_one(self):
        self.assertEqual(multiply(5, 1), 5)
        self.assertEqual(multiply(1, 5), 5)


if __name__ == "__main__":
    unittest.main()
