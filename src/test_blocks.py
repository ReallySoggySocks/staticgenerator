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
        h_space_two = "What about # This?"
        only_h = "#####"
        self.assertEqual(block_to_blocktype(h0), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(h1), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h2), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h3), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h4), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h5), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h6), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h7), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(h_space), BlockType.HEADING)
        self.assertEqual(block_to_blocktype(h_space_two), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(only_h), BlockType.PARAGRAPH)
        
    def test_code_block(self):
        code = "``` print('Hello, world!') ```"
        not_code = "``` print('Hello, world!')"
        not_code_either = "print('Hello, world!') ```"
        self.assertEqual(block_to_blocktype(code), BlockType.CODE_BLOCK)
        self.assertEqual(block_to_blocktype(not_code), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(not_code_either), BlockType.PARAGRAPH)

    def test_quote_block(self):
        quote = "> This is a quote\n> This is also a quote"
        not_a_quote = "> This is a quote\nBut this one isn't"
        self.assertEqual(block_to_blocktype(quote), BlockType.QUOTE)
        self.assertEqual(block_to_blocktype(not_a_quote), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        un_list = "- This is a \n- Unordered list"
        p_list = "-This is not\n-An unordered list"
        p_list_two = "- Neither\n-Is this"
        self.assertEqual(block_to_blocktype(un_list), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_blocktype(p_list), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(p_list_two), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        o_list = "1. This\n2. Is\n3. An\n4. Ordered list"
        p_list = "1.This\n2.Is\n3.not"
        p_lst = " 1. Neither\n 2. Is\n 3. This"
        p_lst_two = "1. Or\n3. This"
        self.assertEqual(block_to_blocktype(o_list), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_blocktype(p_list), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(p_lst), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype(p_lst_two), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()