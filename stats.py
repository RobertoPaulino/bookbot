def get_number_of_words(book_text):
    list_of_words = book_text.split()
    return len(list_of_words)

def sort_on(items):
    return items["num"]

def get_instances_of_characters(book_text):
    lowered_string = book_text.lower()
    character_dict = {}
    character_dict_list = []

    for char in lowered_string:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1


    for entry in character_dict:
        character_dict_list.append({"name": f"{entry}", "num":character_dict[entry]})

    character_dict_list.sort(reverse=True, key=sort_on)

    return character_dict_list
