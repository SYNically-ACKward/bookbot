def get_num_words(text: str):
    new_lst = text.split()
    return len(new_lst)


def character_counter(text: str):
    chars = set(list(text.lower()))
    char_count = {}
    for char in chars:
        char_count[char] = text.lower().count(char)
    return char_count


def structure_data(input: dict):
    output_list = []
    for entry in input:
        if entry.isalpha():
            output_list.append({entry: input.get(entry)})

    return sorted(output_list, key=lambda d: list(d.values())[0], reverse=True)