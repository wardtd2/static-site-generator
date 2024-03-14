import unittest

from block_nodes import block_to_html_code, block_to_html_heading, block_to_html_ordered_list, block_to_html_paragraph, block_to_html_quote, block_to_html_unordered_list, markdown_to_blocks, block_to_block_type, block_type_code, block_type_heading, block_type_ordered_list, block_type_unordered_list, block_type_quote, block_type_paragraph
from htmlnode import LeafNode, ParentNode


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
    def test_block_to_block_type_heading(self):
        md = "###### banana"
        self.assertEqual(block_type_heading, block_to_block_type(md))


    def test_block_to_block_type_code(self):
        md = "``` banana ```"
        self.assertEqual(block_type_code, block_to_block_type(md))
    

    def test_block_to_block_type_quote(self):
        md = "> banana\n> apple\n> orange"
        self.assertEqual(block_type_quote, block_to_block_type(md))
    

    def test_block_to_block_type_unordered_list(self):
        md = "* apple\n* orange\n* banana"
        self.assertEqual(block_type_unordered_list, block_to_block_type(md))


    def test_block_to_block_type_ordered_list(self):
        md = "1. apple\n2. orange\n3. banana"
        self.assertEqual(block_type_ordered_list, block_to_block_type(md))
    

    def test_block_to_block_type_paragraph(self):
        md = "1. apple\n2. orange\n. banana"
        self.assertEqual(block_type_paragraph, block_to_block_type(md))

    
    def test_block_to_html_quote(self):
        md = "> banana\n> apple\n> orange"
        self.assertEqual(LeafNode("blockquote", "banana\napple\norange"), block_to_html_quote(md))


    def test_block_to_html_heading(self):
        md = "###### banana"
        self.assertEqual(LeafNode("h6", "banana"), block_to_html_heading(md))


    def test_block_to_html_code(self):
        md = "``` banana ```"
        inner = LeafNode("code", " banana ")
        outer = ParentNode("pre", [inner])
        self.assertEqual(outer, block_to_html_code(md))


    def test_block_to_html_unordered_list(self):
        md = "* apple\n* orange\n* banana"
        self.assertEqual(LeafNode("ul", "<li>apple\n<li>orange\n<li>banana"), block_to_html_unordered_list(md))


    def test_block_to_html_ordered_list(self):
        md = "1. apple\n2. orange\n3. banana"
        self.assertEqual(LeafNode("ol", "<li>apple\n<li>orange\n<li>banana"), block_to_html_ordered_list(md))


    def test_block_to_html_paragraph(self):
        md = "1. apple\n2. orange\n. banana"
        self.assertEqual(LeafNode("p", "1. apple\n2. orange\n. banana"), block_to_html_paragraph(md))


    def test_markdown_to_html_node(self):
        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        expected = ParentNode("div"[])