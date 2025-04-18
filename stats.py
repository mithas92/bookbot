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
