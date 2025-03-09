from stats import get_num_words, sort_dict, get_num_char
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

bookpath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = get_num_words(get_book_text(bookpath))
    num_chars = get_num_char(get_book_text(bookpath))
    sorted_chars = sort_dict(num_chars)
    print(f"============ BOOKBOT ============ \n Analyzing book found at {bookpath}... \n ----------- Word Count ---------- \n Found {num_words} total words \n --------- Character Count -------")
    for c in sorted_chars:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")

main()