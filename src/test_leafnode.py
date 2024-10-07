import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_basic_leaf_node(self):
        node = LeafNode(tag="p", value="Hello, world!", props=None)
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')

    def test_leaf_node_with_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me!</a>')

    def test_leaf_node_without_tag(self):
        node = LeafNode(tag=None, value="Just text", props=None)
        self.assertEqual(node.to_html(), 'Just text')

    def test_value_error_on_missing_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="p", value=None, props=None)
            node.to_html()

if __name__ == "__main__":
    unittest.main()
