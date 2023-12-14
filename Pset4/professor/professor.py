import random


def main():
    score = 0
    level = get_level()

    for i in range(10):
        user_answer = 0
        tries = 0

        x, y = generate_integer(level), generate_integer(level)
        answer = x + y

        while True:
            try:
                if tries == 3:
                    print(f"{x} + {y} = {answer}")
                    break
                user_answer = int(input(f"{x} + {y} = "))

                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                continue

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level in range(1, 3 + 1):
            break

    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, (10**level) - 1)
    return random.randint(10 ** (level - 1), (10**level) - 1)


if __name__ == "__main__":
    main()
