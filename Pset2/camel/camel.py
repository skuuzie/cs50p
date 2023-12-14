def main():

    camel = input("camelCase: ")
    snake = ""

    for word in camel:
        if word.isupper():
            snake += "_"
            snake += word.lower()
        else:
            snake += word

    print(f"snake_case: {snake}")

main()
