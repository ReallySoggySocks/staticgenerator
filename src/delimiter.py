import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not isinstance(old_nodes, list):
        raise Exception("Node must be in a list")
    
    new_nodes = []
    delimiter_counter = 0

    for node in old_nodes:
        for char in node.text:
            if char == delimiter:
                delimiter_counter += 1

    if delimiter_counter % 2 != 0:
        raise Exception("Invalid markdown syntax")
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = node.text.split(delimiter)

        for text in split_nodes:
            if text == "":
                continue
            elif not text.startswith(" ") and not text.endswith(" "):
                new_nodes.append(TextNode(text, text_type))
            else:
                new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
            
        current_text = node.text
        for alt_text, url in images:
            full_image_markdown = f"![{alt_text}]({url})"
            
            parts = current_text.split(full_image_markdown, 1)
            
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            current_text = parts[1] if len(parts) > 1 else ""
        
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        images = extract_markdown_links(node.text)
        if not images:
            new_nodes.append(node)
            continue
            
        current_text = node.text
        for alt_text, url in images:
            full_link_markdown = f"[{alt_text}]({url})"
            
            parts = current_text.split(full_link_markdown, 1)
            
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.LINK, url))
            
            current_text = parts[1] if len(parts) > 1 else ""
        
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes

def text_to_textnodes(text):

    node = TextNode(text, TextType.TEXT)

    after_bold = split_nodes_delimiter([node], "*", TextType.BOLD)
    after_italic = split_nodes_delimiter(after_bold, "_", TextType.ITALIC)
    after_code = split_nodes_delimiter(after_italic, "`", TextType.CODE)
    after_image = split_nodes_image(after_code)
    after_link = split_nodes_link(after_image)

    return after_link

def markdown_to_blocks(markdown):
    blocks = []
    split_md = markdown.split("\n\n")
    for line in split_md:
        line = line.strip("\n")
        blocks.append(line)

    return blocks