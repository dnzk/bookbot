from stats import count_words, count_unique_chars, sort_chars_by_count
import sys
import os


def get_book_text(path: str) -> str:
    if type(path) != str:
        raise TypeError()
    with open(path) as f:
        return f.read()


def main():
    if sys.argv.__len__() < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]

    if not os.path.isfile(book_path):
        raise FileNotFoundError("incorrect path")

    print(f"Analyzing book found at {book_path}")
    book_text = get_book_text(f"{book_path}")
    word_counts = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")
    unique_chars = count_unique_chars(book_text)
    for entry in sort_chars_by_count(unique_chars):
        if "char" not in entry and "num" not in entry:
            continue
        if not entry["char"].isalpha():
            continue
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main()
