def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)

def word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    word_list = file_contents.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")
    return word_count


word_count("./books/frankenstein.txt")


#main()
