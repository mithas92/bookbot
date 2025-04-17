def get_book_text(book_name):
    with open(book_name) as f:
        file_contents = f.read()
    return file_contents

def count_book_words(book_name):
    with open(book_name) as f:
        file_contents = f.read()
    words_list = file_contents.split()

    return len(words_list)

def main():
    # frankenstein_book = get_book_text("books/frankenstein.txt")
    frankenstein_word_count = count_book_words("books/frankenstein.txt")
    print(f"{frankenstein_word_count} words found in the document")
    return

main()