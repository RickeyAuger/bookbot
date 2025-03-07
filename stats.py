def read_file(filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(file_contents):
    word_list = file_contents.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")
    return word_count



