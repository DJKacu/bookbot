from stats import count, sortu_sortu
def report():
    A = sortu_sortu()
    for i in A:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count()
    print("--------- Character Count -------")
    report()
    print("============= END ===============")

main()