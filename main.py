import sys
from stats import count, sortu_sortu, report

def main():
    try:
        sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    x = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {x}")
    print("----------- Word Count ----------")
    count(x)
    print("--------- Character Count -------")
    report(x)
    print("============= END ===============")

if __name__ == "__main__":
    main()