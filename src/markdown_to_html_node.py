from blocks import *
from splitting_functions import *
from htmlnode import *
from textnode import *
import re

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    md_children = []

    for block in md_blocks:
        md_block_type = block_to_blocktype(block)

        if md_block_type == BlockType.PARAGRAPH:
            block_text = block.replace("\n", " ")
            md_block = ParentNode("p", text_to_children(block_text))

        elif md_block_type == BlockType.CODE_BLOCK:
            md_block = ParentNode("pre", [text_node_to_html_node(TextNode(block.strip("```").lstrip("\n"), TextType.CODE))])

        elif md_block_type == BlockType.HEADING:
            counter = 0
            for char in block:
                if char == "#":
                    counter += 1
                if char == " ":
                    break
            heading_text = block[counter:].strip()
            md_block = ParentNode(f"h{counter}", text_to_children(heading_text))

        elif md_block_type == BlockType.ORDERED_LIST:
            list_children = []
            lines = block.split("\n")
            for line in lines:
                if line.strip():
                    match = re.match(r"^\d+\. ", line)
                    if match:
                        cleaned_line = line[match.end():].strip()
                    else:
                        cleaned_line = line.strip()
                    line_children = text_to_children(cleaned_line)
                    list_children.append(ParentNode("li", line_children))
            md_block = ParentNode("ol", list_children)

        elif md_block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []
            for line in lines:
                if line.strip():
                    if line.startswith("> "):
                        cleaned_lines.append(line[2:].strip())
                    else:
                        cleaned_lines.append(line.strip())
            quote_text = "\n".join(cleaned_lines)
            md_block = ParentNode("blockquote", text_to_children(quote_text))

        elif md_block_type == BlockType.UNORDERED_LIST:
            list_children = []
            lines = block.split("\n")
            for line in lines:
                if line.strip():
                    if line.startswith("* ") or line.startswith("- "):
                        cleaned_line = line[2:].strip()
                    else:
                        cleaned_line = line.strip()
                    print(cleaned_line)
                    line_children = text_to_children(cleaned_line)
                    list_children.append(ParentNode("li", line_children))
            md_block = ParentNode("ul", list_children)
        md_children.append(md_block)

    return ParentNode("div", md_children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    node_list =[]
    for node in text_nodes:
        node_list.append(text_node_to_html_node(node))
    return node_list
    