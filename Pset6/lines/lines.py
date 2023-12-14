import sys

argv, argv_length = sys.argv, len(sys.argv)

if argv_length < 2:
    sys.exit("Too few command-line arguments")
elif argv_length > 2:
    sys.exit("Too many command-line arguments")


def main(filename):
    line_count = 0

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        sys.exit("File does not exist")

    for line in file.readlines():
        line = line.lstrip()

        if len(line) == 0:
            continue
        elif line[0] == "#":
            continue

        line_count += 1

    print(line_count)


if __name__ == "__main__":
    filename = argv[1]

    if filename.split(".")[-1] != "py":
        sys.exit("Not a Python file")

    main(filename)
