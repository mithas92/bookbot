from stats import count_book_words, charec_count, organize_charec

def main():
    # frankenstein_book = get_book_text("books/frankenstein.txt")
    the_book = "books/frankenstein.txt"

    frankenstein_word_count = count_book_words(the_book)

    frankenstein_char_count = charec_count(the_book)

    frankenstein_chars_sorted = organize_charec(frankenstein_char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_word_count} total words")
    print("--------- Character Count -------")

    for charec in frankenstein_chars_sorted:
        if charec["char"].isalpha():
            print(f"{charec["char"]}: {charec["value"]}")

    print("============= END ===============")

    return

main()