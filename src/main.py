from leafnode import *

def main():
    test = LeafNode(tag="a", value="Click me!", props={"href": "https://example.com"})
    print(f"{test.to_html()}")

if __name__ == "__main__":
    main()