import leapyear
import pytest

import unittest
import leapyear

class TestCaseleapyear(unittest.TestCase):
    def test_leapyear_good(self):
        self.assertEqual(leapyear.is_leapyear(2020), True)
        self.assertEqual(leapyear.is_leapyear(2021), False)
        self.assertEqual(leapyear.is_leapyear(100), False)
        self.assertEqual(leapyear.is_leapyear(400), True)
    
    def test_leapyear_fail(self):
        self.assertEqual(leapyear.is_leapyear(1), True)
    
    def test_leapyear_exceptions(self):
        self.assertRaises(TypeError, leapyear.is_leapyear, 'asdf')
        self.assertRaises(ValueError, leapyear.is_leapyear, -4)


if __name__ == '__main__':
    unittest.main()
