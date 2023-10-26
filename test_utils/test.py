import unittest
from test_utils.utils import check_word_list, simplify_words,load_companies

class LoadCompaniesTests(unittest.TestCase):
    
    def test_basic(self):
        companies = load_companies()
        self.assertIsNotNone(companies)

class CheckWordListTests(unittest.TestCase):
   
   def test_all_good(self):
        words = ['hello', 'world', 'python', 'unittest']
        self.assertTrue(check_word_list(words))
   
   def test_with_spaces(self):
        words = ['hello world ', 'world', 'python', 'unit test']
        self.assertFalse(check_word_list(words))

class SimplifyWordsListTEst(unittest.TestCase):
    
    def test_no_change(self):
        words = ['hello', 'world', 'python', 'unittest']
        results = simplify_words(words)
        self.assertEqual(words, results)
    
    def test_has_space(self):
        words = ['hello world ', 'world', 'python', 'unit test']
        results = simplify_words(words)
        self.assertEqual(results[0], 'helloworld')

    
if __name__ == "__main__":
    unittest.main()