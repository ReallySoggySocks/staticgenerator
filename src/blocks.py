from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1,
    HEADING = 2,
    CODE = 3,
    QUOTE = 4,
    UNORDERED_LIST = 5,
    ORDERED_LIST = 6

def block_to_blocktype(block):
    #check if block starts with 1-6 # and a space
    if block.startswith("#"):
        if block.split("# ") and len(block.split("# ")[0]) <= 5:
            return BlockType.HEADING
        else:
            return BlockType.PARAGRAPH
        
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    #check that every line contains >
    elif block.startswith(">"):
        for line in block:
            if line.startswith(">"):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    #check that every line starts with "- "
    elif block.startswith("- "):
        for line in block:
            if line.startswith("- "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    #check that line starts at "1. " and increments each line
    elif block.startswith("1. "):
        line_counter = 1
        for line in block:
            if line[0] == f"{line_counter}":
                line_counter += 1
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    
    else:
        return BlockType.PARAGRAPH