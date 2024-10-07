from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if not self.value:
            raise ValueError
        if self.props:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        elif self.tag:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return str(self.value)