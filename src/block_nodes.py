from htmlnode import LeafNode
from textnode import TextNode

def markdown_to_blocks(markdown):
    blocks = []
    strings = markdown.split("\n\n")
    for string in strings:
        if string == "":
            continue
        string = string.strip()
        blocks.append(string)
    return blocks