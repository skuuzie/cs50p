import sys

from pyfiglet import Figlet

font = "weird"

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 3:
        command = sys.argv[1]

        if command == "-f" or command == "--font":
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

try:
    f = Figlet(font=font)
except:
    sys.exit("Invalid usage")

def main():
    text = input("Input: ")
    print(f"Output:\n{f.renderText(text)}")

main()
