from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    QUOTE = 3
    UNORDERED_LIST = 4
    ORDERED_LIST = 5
    CODE_BLOCK = 6

def block_to_blocktype(block):
    #check if block starts with 1-6 # and a space
    if block.startswith("#"):
        hash_counter = 0
        for char in block:
            if char == "#":
                hash_counter += 1
            if char == " " or hash_counter == 7:
                break
        if hash_counter <= 6 and len(block) > hash_counter and block[hash_counter] == " ":
            return BlockType.HEADING
        else:
            return BlockType.PARAGRAPH
        
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE_BLOCK
    
    #check that every line contains >
    elif block.startswith(">"):
        for line in block.split("\n"):
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    #check that every line starts with "- "
    elif block.startswith("- "):
        for line in block.split("\n"):
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    #check that line starts at "1. " and increments each line
    elif block.startswith("1. "):
        line_counter = 1
        for line in block.split("\n"):
            if not line.startswith(f"{line_counter}. "):
                return BlockType.PARAGRAPH
            
            line_counter += 1
        return BlockType.ORDERED_LIST
    
    else:
        return BlockType.PARAGRAPH