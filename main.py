
def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()

    return text

def get_number_of_words(book_text):
    list_of_words = book_text.split()
    return len(list_of_words)

def main():
    num_of_words = get_number_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_of_words} words found in the document")


main()
