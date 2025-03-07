def read_file(filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(file_contents):
    word_list = file_contents.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")
    return word_count

def get_characters(file_contents):
    lower = file_contents.lower()
    characters = list(file_contents.lower())
    return characters

def char_count(lower_list):
    character_counts = {}
    for c in lower_list:
        if c in character_counts:
            character_counts[c] += 1
        else:
            character_counts[c] = 1
    return character_counts

filepath = "./books/frankenstein.txt"
file_contents = read_file(filepath)
lower_list = get_characters(file_contents)
char_count_dict = char_count(lower_list)



print(char_count_dict)



