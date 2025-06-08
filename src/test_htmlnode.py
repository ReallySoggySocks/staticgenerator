import unittest

from htmlnode import *
from textnode import *

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
    
    def test_leaf_value(self):
        with self.assertRaises(ValueError):
            LeafNode().to_html()
    
    def test_leaf_props(self):
        node = LeafNode("p", "Hello, world!", {"href" : "https://www.google.com"})
        self.assertEqual(node.to_html(), '<p href="https://www.google.com">Hello, world!</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_children(self):
        node = ParentNode("b")
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_no_tag(self):
        child_node = LeafNode("p", "this is a child node")
        node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_mixed_children(self):
        grandchild_node = LeafNode("b", "grandchild")
        y_cousin_node = LeafNode("a", "cousin")
        y_child_node = LeafNode("b", "youngest")
        m_child_node = ParentNode("f", [grandchild_node, y_cousin_node])
        o_child_node = LeafNode("span", "oldest")
        parent_node =  ParentNode("p", [o_child_node, m_child_node, y_child_node])
        g_parent_node = ParentNode("h1", [parent_node])
        self.assertEqual(
            g_parent_node.to_html(),
            "<h1><p><span>oldest</span><f><b>grandchild</b><a>cousin</a></f><b>youngest</b></p></h1>"
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_wrong_type(self):
        with self.assertRaises(Exception):
            node = TextNode("This is a tetx node", TextType.BLAND)

    def test_textnode_image(self):
        node = TextNode("This is a text node", TextType.IMAGES, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src" : node.url, "alt" : node.text})

    def test_textnode_link(self):
        node = TextNode("This is a text node", TextType.LINKS, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href" : "https://www.google.com"})


if __name__ == "__main__":
    unittest.main()