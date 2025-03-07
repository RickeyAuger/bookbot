def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    word_list = file_contents.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")
    return word_count
