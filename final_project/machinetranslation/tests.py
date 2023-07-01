"""Test translation functions"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):
    """Unit tests for translation functions"""

    def test_english_to_french(self):
        """Test translation from English to French"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        """Test translation from French to English"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
