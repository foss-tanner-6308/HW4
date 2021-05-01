import unittest
from cube import *


class TestCase(unittest.TestCase):
    def test_pos(self):
        self.assertAlmostEqual(volume(2), 8)
        self.assertAlmostEqual(volume(4), 64)

    def test_neg(self):
        self.assertAlmostEqual(volume(-2), 8)

    def test_input_not_int(self):
        self.assertAlmostEqual(volume("asdf"), 8)
        self.assertRaises(TypeError, volume, True)


if __name__ == "__main__":
    unittest.main()