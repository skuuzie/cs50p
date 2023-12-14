def main():
    fuel = input("Fraction: ")

    percentage = convert(fuel)
    indicator = gauge(percentage)

    print(indicator)

def convert(fraction):

    fraction = fraction.split("/")

    x, y = int(fraction[0]), int(fraction[1])

    if x > y:
        raise ValueError("Fuel can't be higher than 100%")

    if y == 0:
        raise ZeroDivisionError("Can't divide by 0")

    percentage = int(round(x/y, 2) * 100)

    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
