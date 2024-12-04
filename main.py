def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sorting(chars_dict)
    print(sorted_chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char in sorted_chars:
        print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def sorting(dict):
    sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
