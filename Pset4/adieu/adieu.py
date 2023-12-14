def main():
    pre = "Adieu, adieu, to"
    names = []
    text = pre

    while True:
        try:
            name = input("Name: ")
            names.append(name.strip())
        except EOFError:
            break

    if len(names) == 1:
        text += f" {names[0]}"
    elif len(names) == 2:
        text += f" {names[0]} and {names[1]}"
    else:
        for i in range(len(names)):
            if i == len(names) - 1:
                text += f", and {names[i]}"
                break

            if i == 0:
                text += f" {names[i]}"
            else:
                text += f", {names[i]}"

    print(text)


main()
