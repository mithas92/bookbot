def get_book_text(book_name):
    with open(book_name) as f:
        file_contents = f.read()
    return file_contents

def charec_count(book_name):
    with open(book_name) as f:
        file_contents = f.read()
    
    file_contents = file_contents.lower()

    char_dict = {}
    for c in file_contents:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict

def count_book_words(book_name):
    with open(book_name) as f:
        file_contents = f.read()
    words_list = file_contents.split()

    return len(words_list)

def sort_on(dict_in):
    return dict_in["value"]

def organize_charec(chars_dict):
    
    #Create a sortable list of dictionaries. The sorting item can easily be accessed. 
    all_chars_list = []
    for key, value in chars_dict.items():
        all_chars_list.append({"char": key, "value" :value})

    all_chars_list.sort(reverse=True, key=sort_on)

    return all_chars_list

