import re

um_regex = r"\W?\bum\b\W?"

def main():
    print(count(input("Text: ")))

def count(s):
    return len(re.findall(um_regex, s, re.IGNORECASE))

if __name__ == "__main__":
    main()
