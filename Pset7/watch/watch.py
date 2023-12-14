import re

url_regex = r"""src=\"([^\"]*)\""""


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.findall(url_regex, s)

    if match:
        match = match[0]
        if "youtube" not in match:
            return None
        return f"https://youtu.be/{match.split("/")[-1]}"

    return None


if __name__ == "__main__":
    main()
