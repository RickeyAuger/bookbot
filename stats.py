def read_file(filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(file_contents):
    word_list = file_contents.split()
    word_count = len(word_list)
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

def char_dict_to_sorted_list(char_count_dict):
    chars_list = []
    for char, count in char_count_dict.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

#filepath = sys.argv[1]
#file_contents = read_file(filepath)
#lower_list = get_characters(file_contents)
#char_count_dict = char_count(lower_list)
#char_dict_list = (char_dict_to_sorted_list(char_count_dict))










