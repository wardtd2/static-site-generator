import unittest

from block_nodes import markdown_to_blocks

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TestBlockNodes(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = '''
        # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
        '''
        self.assertEqual(markdown_to_blocks(markdown), ["# This is a heading",
                                                         "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                                                         "* This is a list item\n* This is another list item"])
    

    def test_markdown_to_blocks_longer(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        self.assertEqual(markdown_to_blocks(markdown), ["This is **bolded** paragraph",
                                                         "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                                                         "* This is a list\n* with items"])
    