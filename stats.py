def get_book_text(x):
    with open(x) as f:
        file_contents = f.read()
        return file_contents

def count(x):
    num_words = 0
    words = get_book_text(x).split()
    for i in words:
        num_words += 1
    return print(f"Found {num_words} total words")

def organize(x):
    words = get_book_text(x).lower()
    dict = {}
    for i in words:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

def sort_on(items):
    return items["num"]

def sortu_sortu(x):
    do_sortu = []
    char_dict = organize(x)
    for i in char_dict:
        data = {}
        data["char"] = i
        data["num"] = char_dict[i]
        do_sortu.append(data)
    do_sortu.sort(reverse=True, key=sort_on)
    return do_sortu

def report(x):
    A = sortu_sortu(x)
    for i in A:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")