def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) > 6 or len(s) < 2:
        return False

    if not s.isalnum():
        return False

    if s[:2].isnumeric():
        return False

    num_exist = False

    for pos in range(len(s)):
        if s[pos].isnumeric():
            if not num_exist and s[pos] == "0":
                return False
            else:
                num_exist = True
        elif s[pos].isalpha() and num_exist:
            return False

    return True


if __name__ == "__main__":
    main()
