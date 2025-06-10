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
        split_nodes = node.text.split(delimiter)

        for text in split_nodes:
            if " " not in text:
                new_nodes.append(TextNode(text, text_type))
            else:
                new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def exctract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    if not isinstance(old_nodes, list):
        raise Exception("Node must be in a list")
    
    new_nodes = []

    for node in old_nodes:
        split_nodes = re.split(r"\!\[(.*?)\)", node.text)
        
        for i in range(len(split_nodes) - 1):
            if i % 2 == 0:
                new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
            else:
                text_url = re.split(r"\]\(", split_nodes[i])
                new_nodes.append(TextNode(text_url[0], TextType.IMAGES, text_url[1]))
    return new_nodes

def split_nodes_links(old_nodes):
    if not isinstance(old_nodes, list):
        raise Exception("Node must be in a list")
    
    new_nodes = []

    for node in old_nodes:
        split_nodes = re.split(r"\[(.*?)\)", node.text)
        
        for i in range(len(split_nodes) - 1):
            if i % 2 == 0:
                new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
            else:
                text_url = re.split(r"\]\(", split_nodes[i])
                new_nodes.append(TextNode(text_url[0], TextType.LINKS, text_url[1]))
    return new_nodes