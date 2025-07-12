import unittest
from demographic_data_analyzer import demographic_data_analyzer

class DemographicDataAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.result = demographic_data_analyzer()

    def test_average_age_men(self):
        self.assertIsInstance(self.result['average_age_men'], float)

    def test_percentage_bachelors(self):
        self.assertIsInstance(self.result['percentage_bachelors'], float)

    def test_min_work_hours(self):
        self.assertIsInstance(self.result['min_work_hours'], int)

    def test_race_count(self):
        self.assertTrue("White" in self.result['race_count'])

    def test_highest_earning_country_percentage(self):
        self.assertGreaterEqual(self.result['highest_earning_country_percentage'], 0)

if __name__ == "__main__":
    unittest.main()
