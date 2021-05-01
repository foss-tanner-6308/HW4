import unittest
from name import *


class TestCase(unittest.TestCase):

    # test if name created properly
    def test_works(self):
        self.assertEqual(full_name("Tanner", "Foss"), "Tanner Foss")

    # test if incorrect expected output is caught
    def test_bad(self):
        self.assertEqual(full_name("Tanner", "Foss"), "Tanner Jacob")

    # test if numbers in the name are caught
    def test_int(self):
        self.assertEqual(full_name("Tann3r", "F0ss"), "Tann3r F0ss")


if __name__ == "__main__":
    unittest.main()
