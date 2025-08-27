import unittest
from generate_page import *


class TestGeneratePage(unittest.TestCase):
    def test_title(self):
        h1 = extract_title("# Hello")

        self.assertEqual(h1, "Hello")
        with self.assertRaises(Exception):
            extract_title("Hello")
            extract_title("## Hello")
            extract_title("# ")