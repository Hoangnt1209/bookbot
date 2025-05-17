def get_num_words(text):
    text = text.split()
    return len(text)


def get_num_chars(text):
    chars_dict ={}
    for char in text.lower():
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def get_key_value_pairs(dictionary):
    lst =[]
    for key, value in dictionary.items():
        if key.isalpha():
            lst.append({"char":key, "count":value})
    lst.sort(key=lambda x: x["count"], reverse=True)
    return lst