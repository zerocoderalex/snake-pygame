import unittest
from main import reminder

class TestCheck(unittest.TestCase):
    def test_reminder(self):
        self.assertEqual(reminder(5, 2), 1)
        self.assertEqual(reminder(20, 4), 0)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, reminder, 6, 0)

if __name__ == '__main__':
    unittest.main()