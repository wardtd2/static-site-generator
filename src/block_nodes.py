from htmlnode import LeafNode
from textnode import TextNode

def markdown_to_blocks(markdown):
    blocks = []
    strings = markdown.split("\n")
    offset = 0
    current = ""
    for i in range(0, len(strings)):
        strings[i+ offset] = strings[i + offset].strip()
        if strings[i + offset] == "":
            strings.remove(strings[i + offset])
            offset -= 1
            if current != "":
                blocks.append(current)
                current = ""
        else:
            if current != "":
                current += "\n"
            current += strings[i + offset]
    return blocks