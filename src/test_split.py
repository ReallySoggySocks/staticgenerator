import unittest

from delimiter import *
from textnode import *

class TestSplitDelimiter(unittest.TestCase):
    def test_output(self):
        node = TextNode("This is *bold* text", TextType.TEXT)
        split_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(
            split_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_unmatching_delimiter(self):
        node = TextNode("This is *bold text", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()