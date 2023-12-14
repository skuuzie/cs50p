def main():
    groceries = {}

    while True:
        try:
            item = input().upper()

            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            print()
            for item in sorted(groceries.items()):
                name = item[0]
                count = item[1]
                print(f"{count} {name}")
            break


main()
