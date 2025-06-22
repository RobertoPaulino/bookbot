def get_number_of_words(book_text):
    list_of_words = book_text.split()
    return len(list_of_words)

def get_instances_of_characters(book_text):
    lowered_string = book_text.lower()
    character_dict = {}

    for char in lowered_string:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1

    return character_dict
