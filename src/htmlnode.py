from textnode import TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop = ""
        for item in self.props:
            prop += f' {item}="{self.props[item]}"'
        return prop
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        else:
            return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):

        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        elif not self.tag:
            return f"{self.value}"
        elif self.props:
            prop = self.props_to_html()
            return f"<{self.tag}{prop}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must contain a tag")
        elif not self.children:
            raise ValueError("ParnetNode must contain children")
        else:
            parent_string = f"<{self.tag}>"
            for child in self.children:
                parent_string += child.to_html()
            return parent_string + f"</{self.tag}>"
        

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Not a valid text type")

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINKS:
        return LeafNode("a", text_node.text, {"href" : text_node.url})
    elif text_node.text_type == TextType.IMAGES:
        return LeafNode("img", None, {"src" : text_node.url, "alt" : text_node.text})