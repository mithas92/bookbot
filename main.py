from stats import count_book_words, charec_count

def main():
    # frankenstein_book = get_book_text("books/frankenstein.txt")
    the_book = "books/frankenstein.txt"
    frankenstein_word_count = count_book_words(the_book)
    print(f"{frankenstein_word_count} words found in the document")
    frankenstein_char_count = charec_count(the_book)
    print(frankenstein_char_count)

    return

main()