from re import sub

def main():

    s = input("Word: ")
    shortened = shorten(s)

    print(f"Shortened: {shortened}")


def shorten(word):
    out = ""

    for _word in word:
        out += sub("[^a-zA-Z]", ' ', _word).upper()

    return out

if __name__ == "__main__":
    main()
