from stats import read_file
from stats import get_word_count

filepath = "./books/frankenstein.txt"
file_contents = read_file(filepath)

get_word_count(file_contents)



