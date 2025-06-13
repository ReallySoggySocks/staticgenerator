import unittest

from blocks import *

class TestBlocks(unittest.TestCase):
    def test_heading(self):
        h0 = "This is not a heading"
        h1 = "# This is a heading"
        h2 = "## This is a heading"
        h3 = "### This is a heading"
        h4 = "#### This is a heading"
        h5 = "##### This is a heading"
        h6 = "###### This is a heading"
        h7 = "####### This is not a heading"
        h_space = "# # Is this a heading?"
        self.assertEqual(block_to_blocktype(h0), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(h1), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h2), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h3), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h4), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h5), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h6), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h7), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(h_space), BlockType.HEADING)
        
    def test_code_block(self):
        code = "``` print('Hello, world!') ```"
        not_code = "``` print('Hello, world!')"
        not_code_either = "print('Hello, world!') ```"
        self.assertEqual(block_to_blocktype(code), BlockType.CODE)
        self.assertEqual(block_to_blocktype(not_code), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(not_code_either), BlockType.PARAGRAPH)

    def test_quote_block(self):
        quote = "> This is a quote\n> This is also a quote"
        not_a_quote = "> This is a quote\nBut this one isn't"
        self.assertEqual(block_to_blocktype(quote), BlockType.QUOTE)
        self.assertEqual(block_to_blocktype(not_a_quote), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        pass

    def test_ordered_list(self):
        pass

if __name__ == "__main__":
    unittest.main()