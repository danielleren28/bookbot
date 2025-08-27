# python
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    # python
def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()
