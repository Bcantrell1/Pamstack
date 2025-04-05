import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode("div")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode("a", props={"href": "https://www.google.com", "target": "_blank"})
        # Order of props might vary, so check for both possibilities
        result = node.props_to_html()
        self.assertTrue(
            result == ' href="https://www.google.com" target="_blank"' or 
            result == ' target="_blank" href="https://www.google.com"'
        )

    def test_initialization_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_repr_method(self):
        node = HTMLNode("div", "Hello", [], {"class": "container"})
        expected = "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'container'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
