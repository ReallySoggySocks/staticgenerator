from textnode import *
from copy_static import *

def main():
    garbage = TextNode("some text", TextType.TEXT, "www.bean.com")
    copy_static("./static", "./public")
    print(garbage)

if __name__ == "__main__":
    main()