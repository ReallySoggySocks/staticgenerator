import unittest

from htmlnode import HTMLNode

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
    

if __name__ == "__main__":
    unittest.main()