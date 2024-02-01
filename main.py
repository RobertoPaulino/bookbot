with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    report(file_contents)

def count_words(book):
    words = book.split()
    return (len(words))

def count_letters(book):
    character_dictionary = {}
    for character in book:
        lowered = character.lower()
        if lowered in character_dictionary:
            character_dictionary[lowered] += 1
        else:
            character_dictionary.update({lowered: 1})
    return character_dictionary

def report(book):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(book)} words found in this document")
    print("")
    character_dictionary = count_letters(book)

    for key in character_dictionary:
        print(f"{key} was found {character_dictionary[key]} times")

    print("--- End report ---")



main()