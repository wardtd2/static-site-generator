import re

from htmlnode import LeafNode
from textnode import TextNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"



def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)

    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    raise ValueError("Unrecognized node type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is text_type_text:
            targets = node.text.split(delimiter)

            if len(targets) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            
            for i in range(0, len(targets)):
                if targets[i] == "":
                        continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(targets[i], text_type_text, node.url))
                else:
                    new_nodes.append(TextNode(targets[i], text_type, node.url))
        else:
            new_nodes.append(node)
    
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is text_type_text:
            images = extract_markdown_images(node.text)
            if len(images) == 0:
                new_nodes.append(node)
                continue
            working_text = node.text
            for i in range(0, len(images)):
                split_text = working_text.split(f"![{images[i][0]}]({images[i][1]})", 1)
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], text_type_text, node.url))
                new_nodes.append(TextNode(images[i][0], text_type_image, images[i][1]))
                working_text = split_text[1]
            if working_text != "":
                new_nodes.append(TextNode(working_text, text_type_text, node.url))
        else:
            new_nodes.append(node)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is text_type_text:
            links = extract_markdown_links(node.text)
            if len(links) == 0:
                new_nodes.append(node)
                continue
            working_text = node.text
            for i in range(0, len(links)):
                split_text = working_text.split(f"[{links[i][0]}]({links[i][1]})", 1)
                if split_text[0] != "":
                    new_nodes.append(TextNode(split_text[0], text_type_text, node.url))
                new_nodes.append(TextNode(links[i][0], text_type_link, links[i][1]))
                working_text = split_text[1]
            if working_text != "":
                new_nodes.append(TextNode(working_text, text_type_text, node.url))
        else:
            new_nodes.append(node)
    return new_nodes