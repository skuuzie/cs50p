def main():

    greeting = input("Greeting: ").lower().rstrip().lstrip()

    if greeting[0] != "h" or "h" not in greeting:
        print("$100")
    else:
        if "hello" in greeting:
            print("$0")
        elif greeting[0] == "h":
            print("$20")

main()
