from splitting_functions import markdown_to_blocks
import os
from markdown_to_html_node import *

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    dir_entry = os.listdir(dir_path_content)

    for entry in dir_entry:
        new_start = os.path.join(dir_path_content, entry)
        new_dest = os.path.join(dest_dir_path, entry)

        if os.path.isfile(new_start):
            entry_html = entry.rstrip(".md") + ".html"
            dest_html = os.path.join(dest_dir_path, entry_html)
            generate_page(new_start, template_path, dest_html)
        else:
            os.mkdir(new_dest)
            generate_pages_recursive(new_start, template_path, new_dest)
    
    return

def extract_title(markdown):
    md_blocks = markdown_to_blocks(markdown)
    if md_blocks[0].startswith("# ") and len(md_blocks[0].lstrip("# ")) > 0:
        return md_blocks[0].lstrip("# ")
    else:
        raise Exception("No Header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        md_content = f.read()
    
    with open(template_path, "r") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(md_content)
    content_title = extract_title(md_content)
    html_content = html_content.to_html()

    template_content = template_content.replace("{{ Title }}", f"{content_title}")
    template_content = template_content.replace("{{ Content }}", f"{html_content}")

    with open(dest_path, "w") as f:
        dest_path = f.write(template_content)
        dest_path = f.close()

    return