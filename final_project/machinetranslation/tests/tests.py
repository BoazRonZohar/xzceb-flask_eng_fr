"""
This unit test translator.py
"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        """
        This tests translation from English to French
        """
        # Test when ""Hello" is given as an input the output is "Bonjour"
        self.assertEqual(english_to_french('hello'),'Bonjour')
        # Test when ""sun" is given as an input the output is "Soleil"
        self.assertEqual(english_to_french('sun'),'Soleil')
         # Test when "How are you?"" is given as an input the output is "Comment vas-tu?"
        self.assertEqual(english_to_french('How are you?'),'Comment es-tu?')
        # Test when "sun" is given as input the output is not "Sun"
        self.assertNotEqual(english_to_french('sun'),'Sun')
        # Test for null input for english_to_french
        self.assertIsNotNone(english_to_french('soleil'),'Test value is none')

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        """
        This tests translation from French to English
        """
        # Test when "Bonjour" is given as input the output is "Hello"
        self.assertEqual(french_to_english('bonjour'),'Hello')
        # Test when "Soleil" is given as input the output is "sun"
        self.assertEqual(french_to_english('soleil'),'Sun')
        # Test when "Comment vas-tu?"" is given as an input the output is "How are you?"
        self.assertEqual(french_to_english('Comment es-tu?'),'How are you?')
         # Test when "Soleil" is given as input the output is not "Soleil"
        self.assertNotEqual(french_to_english('soleil'),'Soleil')
        # Test for null input for french_to_english
        self.assertIsNotNone(french_to_english('soleil'),'Test value is none')

unittest.main()
