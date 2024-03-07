from textnode import TextNode



def main():
    test_text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test_text_node)
    print(TextNode.text_node_to_html_node(test_text_node))


main()