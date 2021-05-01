import unittest
from cube import *


class TestCase(unittest.TestCase):

    # test if volume is calculated properly
    def test_pos(self):
        self.assertAlmostEqual(volume(2), 8)

    # make sure negative input is handled
    def test_neg(self):
        self.assertAlmostEqual(volume(-2), 8)

    # make sure non int or float input is handled
    def test_input_not_int(self):
        self.assertAlmostEqual(volume("asdf"), 8)


if __name__ == "__main__":
    unittest.main()