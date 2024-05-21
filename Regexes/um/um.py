import re


def main():
    print(count(input("Text: ")))


def count(s):

    pattern = re.findall(r'\bum\b|\bum(?=\W)',s, re.IGNORECASE)
    return len(pattern)



if __name__ == "__main__":
    main()
