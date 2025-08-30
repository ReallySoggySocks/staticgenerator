from textnode import *
from copy_static import *
from generate_pages_recursive import *

def main():
    copy_static("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()