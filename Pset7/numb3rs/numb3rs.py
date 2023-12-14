import re

ipv4_regex = r"^.[0-9]*\..[0-9]*\..[0-9]*\..[0-9]*$"


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip.isalpha():
        return False

    if match := re.search(ipv4_regex, ip):
        for num in match[0].split("."):
            if int(num) > 255 or int(num) < 0:
                return False
    else:
        return False

    return True


if __name__ == "__main__":
    main()
