import sys
from stats import count_words, count_char, dict_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)
    num_chars = count_char(text)
    report = dict_list(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in report:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")





main()