from stats import get_number_of_words
from stats import get_instances_of_characters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()

    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    num_of_words = get_number_of_words(book_text)
    instances_dict = get_instances_of_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for instance in instances_dict:
        if instance["name"].isalpha():
            print(f"{instance["name"]}: {instance["num"]}")

    print("============= END ===============")


main()
