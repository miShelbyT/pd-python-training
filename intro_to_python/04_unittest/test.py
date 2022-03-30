import unittest
import enumberables


class TestEnumerables(unittest.TestCase):

    def test_spiciest_foods(self):
        self.assertEqual(enumberables.spiciest_foods(), [
      { "name": 'Green Curry', "cuisine": 'Thai', "heat_level": 9 },
      { "name": 'Mapo Tofu', "cuisine": 'Sichuan', "heat_level": 6 } 
    ], '''return a list of hashes where the heat level of the food is greater than 5''')