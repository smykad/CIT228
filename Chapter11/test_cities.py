import unittest
from city_functions import city_country

class CityNamesTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_city = city_country('santiago', 'chilE')
        self.assertEqual(formatted_city, 'Santiago, Chile')
    
    def test_city_country_population(self):
        formatted_city_population = city_country('santiago', 'chile', '5000000')
        self.assertEqual(formatted_city_population, 'Santiago, Chile - Population 5000000')
if __name__ == '__main__':
    unittest.main()