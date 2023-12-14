import sys

from PIL import Image, ImageOps

argv, argv_length = sys.argv, len(sys.argv)

if argv_length < 3:
    sys.exit("Too few command-line arguments")
elif argv_length > 3:
    sys.exit("Too many command-line arguments")

accepted_extension = {"jpeg": 0, "jpg": 0, "png": 0}


def main(in_filename, out_filename):
    try:
        input_image = Image.open(in_filename)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

    shirt_img = Image.open("shirt.png")

    input_image = ImageOps.fit(input_image, shirt_img.size)
    input_image.paste(shirt_img, (0, 0), shirt_img)
    input_image.save(out_filename)


if __name__ == "__main__":
    in_filename, inf_extension = argv[1], argv[1].split(".")[-1]
    out_filename, outf_extension = argv[2], argv[2].split(".")[-1]

    if inf_extension not in accepted_extension:
        sys.exit("Invalid input")

    if outf_extension not in accepted_extension:
        sys.exit("Invalid output")

    if inf_extension != outf_extension:
        sys.exit("Input and output have different extensions")

    main(in_filename, out_filename)
