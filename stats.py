def get_book_text(book_name):
    with open(book_name) as f:
        file_contents = f.read()
    return file_contents

def count_book_words(book_name):
    with open(book_name) as f:
        file_contents = f.read()
    words_list = file_contents.split()

    return len(words_list)
