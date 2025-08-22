def count_words(text):
    return len(text.split())

def count_char(text):
    character_dict = {}
    for char in text.lower():
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def dict_list(count_char):
    result = []
    for char, num in count_char.items():
        result.append({"char": char, "num": num})
    result.sort(reverse=True, key=lambda item: item["num"])
    return result



