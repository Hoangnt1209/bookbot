from stats import get_num_words , get_num_chars, get_key_value_pairs
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = sys.argv[1]

    book_text = get_book_text(file)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    num_chars = get_key_value_pairs(num_chars)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----")
    for char in num_chars:
        print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")
main()