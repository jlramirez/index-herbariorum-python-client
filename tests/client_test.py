import os
import unittest
from indexherbariorum.client import IndexHerbariorumApi


class IndexHerbariorumApiTest(unittest.TestCase):
    """Tests for Index Herbariorum API"""

    def test_countries(self):
        api = IndexHerbariorumApi()
        countries = api.countries()
        self.assertEqual(countries['meta']['code'], 200)

    def test_staff(self):
        api = IndexHerbariorumApi()
        staff = api.staff(rq={'code': 'ny', 'sort': 'lastName'})
        self.assertEqual(staff['meta']['code'], 200)
        with self.assertRaises(Exception):
            api.staff(rq={'download': 'yes'})

    def test_institutions(self):
        api = IndexHerbariorumApi()
        institutions = api.institutions(rq={'country': 'italy', 'city': 'rome', 'sort': 'code'})
        self.assertEqual(institutions['meta']['code'], 200)
        with self.assertRaises(Exception):
            api.institutions(rq={'download': 'yes'})

    def test_institution(self):
        api = IndexHerbariorumApi()
        institution = api.institution('ala')
        self.assertEqual(institution['code'], 'ALA')

    def test_count_countries(self):
        api = IndexHerbariorumApi()
        count = api.count_countries()
        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 0)

    def test_count_staff(self):
        api = IndexHerbariorumApi()
        count = api.count_staff(rq={'country': 'spain', 'correspondent': 'yes'})
        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 0)

    def test_count_institutions(self):
        api = IndexHerbariorumApi()
        count = api.count_institutions(rq={'country': 'bolivia'})
        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 0)

    def test_download(self):
        api = IndexHerbariorumApi()
        api.download('institutions', rq={'country': 'italy', 'city': 'rome'})
        api.download('staff', rq={'state': 'new york', 'correspondent': 'yes'}, filename='staff.csv')
        self.assertTrue(os.path.exists('index_herbariorum.csv'))
        self.assertTrue(os.path.exists('staff.csv'))
        with self.assertRaises(Exception):
            api.download('staff')
            api.download('countries')


if __name__ == '__main__':
    unittest.main()

