from stats import count_book_words

def main():
    # frankenstein_book = get_book_text("books/frankenstein.txt")
    frankenstein_word_count = count_book_words("books/frankenstein.txt")
    print(f"{frankenstein_word_count} words found in the document")
    return

main()