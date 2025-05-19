import unittest
from app.modules.summarizer import Summarizer

class TestSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = Summarizer()

    def test_basic_summary(self):
        result = self.summarizer.summarize("The quick brown fox jumps over the lazy dog. " * 10)
        self.assertIsInstance(result, list)
        self.assertIn('summary_text', result[0])

if __name__ == '__main__':
    unittest.main()
