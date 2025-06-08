from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
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