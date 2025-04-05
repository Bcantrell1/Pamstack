import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_bold_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_norm_eq(self):
        node = TextNode("This is a normal text node", TextType.NORMAL)
        node2 = TextNode("This is a normal text node", TextType.NORMAL)
        self.assertEqual(node, node2)
        
    def test_ital_eq(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        node2 = TextNode("This is a italic text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_code_eq(self):
        node = TextNode("This is a code node", TextType.CODE)
        node2 = TextNode("This is a code node", TextType.CODE)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a image node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    

if __name__ == "__main__":
    unittest.main()
