def stats():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

def get_num_words(text):
    words = text.split()
    return len(words)

get_num_words()