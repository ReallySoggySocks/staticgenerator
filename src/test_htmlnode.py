import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, "this is a htmlnode", None, {"href" : "https://www.google.com", "target" : "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_none(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode(None, "this is a htmlnode", None, {"href" : "https://www.google.com", "target" : "_blank"})
        self.assertEqual(node.__repr__(), "HTMLNode(None, this is a htmlnode, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    

if __name__ == "__main__":
    unittest.main()