import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import read_file
from stats import get_word_count
from stats import get_characters
from stats import char_count
from stats import char_dict_to_sorted_list

filepath = sys.argv[1]

file_contents = read_file(filepath)

lower_list = get_characters(file_contents)

char_count_dict = char_count(lower_list)

word_count = get_word_count(file_contents)

char_dict_list = (char_dict_to_sorted_list(char_count_dict))


print("============ BOOKBOT ============")

print(f"Analyzing book found at {filepath}...")

print("----------- Word Count ----------")

print(f"Found {word_count} total words")

print("----------- Character Count ----------")

for item in char_dict_list:
    if item['char'].isalpha():
        print(f"{item['char']}: {item['count']}")


print("============= END ===============")



