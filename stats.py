def count_words(book):
    num_of_words = 0
    words = book.split()
    num_of_words = len(words)
    return num_of_words

def unique_char_appearances(book):
    char_dict = {}
    low_book = book.lower()
    list(low_book)
    for char in low_book:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort(dictionary):
    dict_list = []
    for entry in dictionary:
        number = dictionary[entry]
        labled_entry = {"char":entry,"num":number}
        dict_list.append(labled_entry)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list