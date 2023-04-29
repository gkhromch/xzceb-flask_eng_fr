import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(), "") 
        self.assertEqual(english_to_french(""), "") 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
 
class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(), "") 
        self.assertEqual(french_to_english(""), "") 
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == '__main__':  #run only directly, not if the module is imported
    unittest.main()

