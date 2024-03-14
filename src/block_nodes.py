from htmlnode import LeafNode
from textnode import TextNode



block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"



def markdown_to_blocks(markdown):
    blocks = []
    strings = markdown.split("\n\n")
    for string in strings:
        if string == "":
            continue
        string = string.strip()
        blocks.append(string)
    return blocks


def block_to_block_type(block):
    first_char = char = block[0]
    if first_char == "#":
        return block_type_heading
    if block[0:3] == "```" and block[-3:] == "```":
        return block_type_code
    if first_char == ">":
        lines = block.split("\n")
        for line in lines:
            if line[0] != ">":
                return block_type_paragraph
        return block_type_quote
    if first_char == "*" or first_char == "-":
        lines = block.split("\n")
        for line in lines:
            if line[0] != first_char:
                return block_type_paragraph
        return block_type_unordered_list
    if first_char == "1":
        lines = block.split("\n")
        index = 1
        for line in lines:
            if line[0:2] != f"{index}.":
                return block_type_paragraph
            index += 1
        return block_type_ordered_list
    return block_type_paragraph

    