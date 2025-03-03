import sys
from stats import get_num_words, character_counter, structure_data


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    output = get_book_text(file_path)
    num_words = get_num_words(output)
    num_chars = character_counter(output)
    stats = structure_data(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in stats:
        key = list(i.keys())[0]
        value = i[key]
        print(f"{key}: {value}")
    print("============= END ===============")
