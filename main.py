from collections import Counter

def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read().lower()  

    print(f"Full text of the book:\n{file_contents[:500]}...\n")

    word_count = count_words(file_contents)
    print(f"Total word count: {word_count}")

    char_count = count_characters(file_contents)
    print_report(char_count, word_count)


def count_words(text):
    return len(text.split())  


def count_characters(text):
    return Counter(filter(str.isalpha, text))


def print_report(char_dict, total_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document\n")

    for char, count in char_dict.most_common():
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()