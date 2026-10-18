import unittest
from calculator import add

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

if __name__ == "__main__":
    unittest.main()
