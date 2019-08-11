import unittest
from views import get_primes

class TestView(unittest.TestCase):
    def test_values(self):
        self.assertEqual(get_primes(13), [2, 3, 5, 7, 11])

    def test_types(self):
        self.assertTrue(get_primes(1212))
        self.assertFalse(get_primes('2313'))