def main():

    greeting = input("Greeting: ")
    val = value(greeting)

    print(f"${val}")

def value(greeting):

    greeting = greeting.strip().lower()

    if greeting[0] != "h" or "h" not in greeting:
        return 0
    else:
        if "hello" in greeting:
            return 100
        elif greeting[0] == "h":
           return 20

if __name__ == "__main__":
    main()
