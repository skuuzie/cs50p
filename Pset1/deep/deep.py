def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

    if answer in ("42", "forty two", "forty-two"):
        print("Yes")
    else:
        if answer.replace(" ", "") == "42":
            print("Yes")
            return
        print("No")

main()
