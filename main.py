from stats import get_number_of_words
from stats import get_instances_of_characters

def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()

    return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_of_words = get_number_of_words(book_text)
    print(f"{num_of_words} words found in the document")
    print(get_instances_of_characters(book_text))

main()
