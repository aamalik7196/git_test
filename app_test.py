"""Unit test file for app.py"""
from app import return_backwards_string
import unittest


class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""

    def dummy_test(self):
        """Test return backwards simple string"""
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed, return_backwards_string(random_string))


if __name__ == "__main__":
    unittest.main()

