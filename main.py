from stats import count_words, unique_char_appearances, sort
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main(filepath):
    book = get_book_text(filepath)
    char_counts = unique_char_appearances(book)
    sorted_counts = sort(char_counts)

    print(
    "============ BOOKBOT ============\n"
    f"Analyzing book found at {filepath}...\n"
    "----------- Word Count ----------\n"
    f"Found {count_words(book)} total words\n"
    "--------- Character Count -------"
    )
    for entry in sorted_counts:
        is_alpah = entry["char"].isalpha()
        if is_alpah == True:
            char = entry["char"]
            num = entry["num"]
            concat = char + ": " + str(num)
            print(concat)
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
