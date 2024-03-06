import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    
    def test_url_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        node2 = TextNode("This is a text node", "bold",  "https://www.google.com")
        self.assertEqual(node, node2)
    
    
    def test_url_specified(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    
    def test_different_style(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    
    def test_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node2)


    def test_different_urls(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        node2 = TextNode("This is a different text node", "bold", "https://www.bing.com")
        self.assertNotEqual(node, node2)

    
    def test_rerp_func(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual("TextNode(This is a text node, bold, https://www.google.com)", repr(node))


if __name__ == "__main__":
    unittest.main()
