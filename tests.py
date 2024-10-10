import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit


class ConversionsTest(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        kelvin = convertCelsiusToKelvin(300)
        expected = 573.15
        self.assertAlmostEqual(kelvin, expected, 2)

    def test_convertCelsiusToKelvin2(self):
        kelvin = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertAlmostEqual(kelvin, expected, 2)

    def test_convertCelsiusToFahrenheit(self):
        f = convertCelsiusToFahrenheit(300)
        expected = 572.0
        self.assertAlmostEqual(f, expected, 2)


if __name__ == '__main__':
    unittest.main()
