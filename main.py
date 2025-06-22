from stats import get_number_of_words
from stats import get_instances_of_characters

def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()

    return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_of_words = get_number_of_words(book_text)
    instances_dict = get_instances_of_characters(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for instance in instances_dict:
        if instance["name"].isalpha():
            print(f"{instance["name"]}: {instance["num"]}")

    print("============= END ===============")


main()
