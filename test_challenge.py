

import unittest
from challenge import reverseString


if __name__ == '__main__':
    unittest.main()


class TestReverseString(unittest.TestCase):

    def test_exists(self):
        self.assertTrue(callable(reverseString))

    def test_returnsString(self):
        self.assertIsInstance(reverseString("a"), str)

    def test_reversesSmallString(self):
        self.assertEqual(reverseString("abc"), "cba")

    def test_rejectsInvalidInput(self):
        self.assertEqual(reverseString(123), TypeError)

    def test_singleCharacter(self):
        self.assertEqual(reverseString("a"), "a")

    def test_twoCharacters(self):
        self.assertEqual(reverseString("ab"), "ba")

    def test_largeString(self):
        self.assertEqual(reverseString("zyxqvutsrqponmlkjihgfedcba"), "abcdefghijklmnopqrstuvqxyz")
