def main():

    text = input("Input: ")
    out = ""

    for word in text:
        if not word.lower() in ("a", "i", "u", "e", "o"):
            out += word

    print(f"Output: {out}")

main()
