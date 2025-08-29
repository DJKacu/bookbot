def get_book_text():
    with open(r"books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count():
    num_words = 0
    words = get_book_text().split()
    for i in words:
        num_words += 1
    return print(f"Found {num_words} total words")

def organize():
    words = get_book_text().lower()
    dict = {}
    for i in words:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

def sort_on(items):
    return items["num"]

def sortu_sortu():
    do_sortu = []
    char_dict = organize()
    for i in char_dict:
        data = {}
        data["char"] = i
        data["num"] = char_dict[i]
        do_sortu.append(data)
    do_sortu.sort(reverse=True, key=sort_on)
    return do_sortu