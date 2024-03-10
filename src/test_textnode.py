import unittest

from textnode import TextNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

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

    
    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ]
        )
    

    def test_split_nodes_invalid_markdown(self):
        with self.assertRaises(Exception):
            node = TextNode("This is text with a `code block word", text_type_text)
            new_nodes = TextNode.split_nodes_delimiter([node], "`", text_type_code)


    def test_split_nodes_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ]
        )


    def test_split_nodes_italics(self):
        node = TextNode("This is text with an *italicized* word", text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italicized", text_type_italic),
                TextNode(" word", text_type_text),
            ]
        )
    

    def test_split_nodes_first_word_delimited(self):
        node = TextNode("*This* is text with an italicized word", text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This", text_type_italic),
                TextNode(" is text with an italicized word", text_type_text),
            ]
        )


    def test_split_nodes_last_word_delimited(self):
        node = TextNode("This is text with an italicized *word*", text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an italicized ", text_type_text),
                TextNode("word", text_type_italic),
            ]
        )


    def test_split_nodes_multiple(self):
        node = TextNode("This is text with *multiple* *italicized* words", text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", text_type_text),
                TextNode("multiple", text_type_italic),                
                TextNode(" ", text_type_text),
                TextNode("italicized", text_type_italic),
                TextNode(" words", text_type_text),
            ]
        )



    def test_split_nodes_multiple_delimiters(self):
        node = TextNode("This is `text` with an *italicized* word", text_type_text)
        new_nodes = TextNode.split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is `text` with an ", text_type_text),
                TextNode("italicized", text_type_italic),
                TextNode(" word", text_type_text),
            ]
        )
    

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(TextNode.extract_markdown_images(text), [
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("another", "https://i.imgur.com/dfsdkjfd.png")
        ])
    

    def test_extract_markdown_text(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(TextNode.extract_markdown_links(text), [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another")
        ])





if __name__ == "__main__":
    unittest.main()
