import sys

argv, argv_length = sys.argv, len(sys.argv)

if argv_length < 3:
    sys.exit("Too few command-line arguments")
elif argv_length > 3:
    sys.exit("Too many command-line arguments")


def main(in_filename, out_filename):
    try:
        file = open(in_filename, "r")
    except FileNotFoundError:
        sys.exit(f"Could not read {in_filename}")

    fstream = open(out_filename, "w")

    fstream.write("first,last,house\n")

    for lines in file.readlines():
        line = lines.split(",")

        if len(line) != 3:
            continue

        first_name = line[1].replace('"', "").strip()
        last_name = line[0].replace('"', "").strip()
        house = line[2]

        proper_line = f"{first_name},{last_name},{house}"
        fstream.write(proper_line)

    fstream.close()


if __name__ == "__main__":
    in_filename = argv[1]
    out_filename = argv[2]

    main(in_filename, out_filename)
