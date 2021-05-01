import unittest
from average import *


class TestCase(unittest.TestCase):

    # test if average calculated properly
    def test_list_good(self):
        self.assertAlmostEqual(avg([1, 1, 1, 3, 4]), 2)

    # test if incorrect expected output recognized
    def test_list_bad(self):
        self.assertAlmostEqual(avg([1, 1, 1, 1, 1]), 5)

    # make sure empty list/divide by 0 is handled
    def test_empty_zero(self):
        self.assertAlmostEqual(avg([]), 0)


if __name__ == "__main__":
    unittest.main()
