def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)

from stats import get_word_count


get_word_count("./books/frankenstein.txt")


#main()
