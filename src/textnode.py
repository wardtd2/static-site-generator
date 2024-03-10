from htmlnode import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    
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
                    if i % 2 == 0:
                        if targets[i] == "":
                            continue
                        new_nodes.append(TextNode(targets[i], text_type_text, node.url))
                    else:
                        if targets[i] == "":
                            continue
                        new_nodes.append(TextNode(targets[i], text_type, node.url))
            else:
                new_nodes.append(node)
        return new_nodes