from textnode import *
from copy_static import *
from generate_page import *

def main():
    copy_static("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")

if __name__ == "__main__":
    main()