def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_counts = get_letter_counts(text)
    print_report(book_path, word_count, letter_counts)


def sort_on(dict):
    return dict["count"]

def print_report(book_path, word_count, letter_counts):
    sorted_letters = []
    for letter in letter_counts:
        sorted_letters.append({"letter": letter, "count":letter_counts[letter]})
    sorted_letters.sort(reverse=True,key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for letter in sorted_letters:
        letter_key = letter["letter"]
        letter_count = letter["count"]
        print(f"The '{letter_key}'  character was found {letter_count} times")
    print("--- End report ---")

def get_letter_counts(text):
    letter_dict = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter.isalpha()==False: #remove to include all characters, not just alpha characters
            continue
        elif lower_letter in letter_dict:
            letter_dict[lower_letter] += 1
        else:
            letter_dict[lower_letter] = 1
    return letter_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

main()
