import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "This is sample text", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "This is sample text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    
    def test_props_to_html(self):
        node = HTMLNode("a", "This is sample text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "This is sample text", {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode("a", "This is sample text", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())


    def test_to_html_with_properties(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())


    #Figuring out how to implement this check
    # def test_throws_value_error_with_empty_value(self):
    #     node = LeafNode("a", None, {"href": "https://www.google.com"})
    #     self.assertRaises(ValueError("Leaf nodes require a value"), node.to_html())



if __name__ == "__main__":
    unittest.main()
