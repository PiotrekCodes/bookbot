from collections import Counter


def main():
    book_path = "books/frankenstein.txt"
    book_name = book_path.split("/")[-1].split(".")[0]
    book_content = read_book(book_path)
    word_count = (count_words(book_content))
    letter_count = (count_letters(book_content))

    print(
        f"The book {book_name} has {word_count} words and {len(letter_count)} different letters."
    )
    print(
        f"The most common letter is {letter_count[0][0]} with {letter_count[0][1]} occurrences."
    )
    print(
        f"The least common letter is {letter_count[-1][0]} with {letter_count[-1][1]} occurrences."
    )


def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    lower_case_text = text.lower()
    count = Counter(lower_case_text)
    del count[" "]
    count = {k: v for k, v in count.items() if k.isalpha()}
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return count


main()
