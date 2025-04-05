from textnode import TextNode, TextType

def main():
    node = TextNode("This is my personal website", TextType.LINK, "https://briancantrell.me")
    print(node)

if __name__ == "__main__":
    main()
