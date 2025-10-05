import unittest
from roman_numerals.int_to_roman import intToRoman
from roman_numerals.roman_to_int import romanToInt


class TestRomanNumerals(unittest.TestCase):
    def test_int_to_roman(self):
        self.assertEqual(intToRoman(3749), "MMMDCCXLIX")
        self.assertEqual(intToRoman(58), "LVIII")
        self.assertEqual(intToRoman(1994), "MCMXCIV")

    def test_roman_to_int(self):
        self.assertEqual(romanToInt("III"), 3)
        self.assertEqual(romanToInt("LVIII"), 58)
        self.assertEqual(romanToInt("MCMXCIV"), 1994)

    def test_bidirectional(self):
        for num in [1, 4, 9, 40, 90, 400, 900, 2024, 3999]:
            roman = intToRoman(num)
            self.assertEqual(romanToInt(roman), num)


if __name__ == "__main__":
    unittest.main()
