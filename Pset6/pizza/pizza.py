import sys

from tabulate import tabulate

argv, argv_length = sys.argv, len(sys.argv)

if argv_length < 2:
    sys.exit("Too few command-line arguments")
elif argv_length > 2:
    sys.exit("Too many command-line arguments")


def main(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        sys.exit("File does not exist")

    data = []

    for line in file.readlines():
        line = line.split(",")
        line[-1] = line[-1].strip()
        data.append(line)

    print(tabulate(data, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    filename = argv[1]

    if filename.split(".")[-1] != "csv":
        sys.exit("Not a CSV file")

    main(filename)
