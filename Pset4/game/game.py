import random


def main():
    guess = -1
    level = -1

    while level < 0 or level > 100:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

    ans = random.randint(1, level + 1)

    while guess != ans:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess > ans:
            print("Too large!")
        elif guess < ans:
            print("Too small!")

    sys.exit("Just Right!")


main()
