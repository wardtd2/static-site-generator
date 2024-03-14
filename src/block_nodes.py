from htmlnode import LeafNode, ParentNode
from inline_nodes import text_node_to_html_node, text_to_textnodes



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
    first_char = block[0]
    if (block[0:2] == "# "
        or block[0:3] == "## "
        or block[0:4] == "### "
        or block[0:5] == "#### "
        or block[0:6] == "##### "
        or block[0:7] == "###### "):
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


def block_to_html_quote(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        cleaned.append(line[1:].strip())
    content = "\n".join(cleaned)
    text_nodes = text_to_textnodes(content)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode("blockquote", html_nodes, None)


def block_to_html_unordered_list(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        cleaned.append(f"{line[1:].strip()}")
        html_nodes = []
    for item in cleaned:
        html_nodes.append(LeafNode("li", item))
    return ParentNode("ul", html_nodes, None)


def block_to_html_ordered_list(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        cleaned.append(f"{line[2:].strip()}")
        html_nodes = []
    for item in cleaned:
        html_nodes.append(LeafNode("li", item))
    return ParentNode("ol", html_nodes, None)


def block_to_html_code(block):
    content = block[3:-3]
    inner_node = LeafNode("code", content, None)
    outer_node = ParentNode("pre", [inner_node], None)
    return outer_node


def block_to_html_heading(block):
    tag = ""
    content = ""
    if block.startswith("# "):
        tag = "h1"
        content = block[2:]
    elif block.startswith("## "):
        tag = "h2"
        content = block[3:]
    elif block.startswith("### "):
        tag = "h3"
        content = block[4:]
    elif block.startswith("#### "):
        tag = "h4"
        content = block[5:]
    elif block.startswith("##### "):
        tag = "h5"
        content = block[6:]
    elif block.startswith("###### "):
        tag = "h6"
        content = block[7:]
    text_nodes = text_to_textnodes(content)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode(tag, html_nodes, None)


def block_to_html_paragraph(block):
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return ParentNode("p", html_nodes)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == block_type_paragraph:
            child_nodes.append(block_to_html_paragraph(block))
        elif type == block_type_code:
            child_nodes.append(block_to_html_code(block))
        elif type == block_type_heading:
            child_nodes.append(block_to_html_heading(block))
        elif type == block_type_quote:
            child_nodes.append(block_to_html_quote(block))
        elif type == block_type_unordered_list:
            child_nodes.append(block_to_html_unordered_list(block))
        elif type == block_type_ordered_list:
            child_nodes.append(block_to_html_ordered_list(block))
    return ParentNode("div", child_nodes)