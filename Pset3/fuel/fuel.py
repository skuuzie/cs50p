def main():

    while True:
        try:
            fuel = input("Fraction: ").split("/")
            fraction = int(fuel[0]) / int(fuel[1])
            percentage = int(round(fraction, 2) * 100)

            if percentage > 100:
                continue

        except (ZeroDivisionError, ValueError):
            pass
        else:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

main()
