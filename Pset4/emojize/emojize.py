import emoji

def main():

    s = input("Input: ")
    emojized = emoji.emojize(s, language="alias")
    print(f"Output: {emojized}")

main()
