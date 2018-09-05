import unittest
from city_country import city_country_func

class CityCountryTestCase(unittest.TestCase):
    def test_city_country_name(self):
        city_country_info = city_country_func('sf', 'usa')
        self.assertEqual(city_country_info, 'sf, usa')

    def test_city_country_pop(self):
        city_country_info = city_country_func('sf', 'usa', '5,108,085')
        self.assertEqual(city_country_info, 'sf, usa has a population of 5,108,085')

unittest.main()
