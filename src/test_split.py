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

    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = exctract_markdown_images(text)
        self.assertEqual(extracted, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted = extract_markdown_links(text)
        self.assertEqual(extracted,[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_no_text(self):
        text = ""
        extracted = exctract_markdown_images(text)
        self.assertEqual(extracted, [])

    def test_split_images(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), 
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGES, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT),
                TextNode("obi wan", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_split_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        self.assertEqual(split_nodes_links([node]),
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")
            ]
        )

    def test_node_not_list(self):
        with self.assertRaises(Exception):
            node = TextNode("text", TextType.TEXT)
            split_nodes_image(node)
            split_nodes_links(node)
            split_nodes_delimiter(node)

if __name__ == "__main__":
    unittest.main()