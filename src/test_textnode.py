import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq_same_properties(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_neq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_neq_different_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    
    def test_neq_different_type(self):
        node = TextNode("This is a text node", "bold")
        not_a_text_node = "I'm just a string"
        self.assertNotEqual(node, not_a_text_node)

    def test_neq_url(self):
        node = TextNode("This is a test node", "bold", "http://test.url")
        node2 = TextNode("This is a test node", "bold")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()