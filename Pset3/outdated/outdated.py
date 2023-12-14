def main():
    months = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12",
    }

    while True:
        try:
            _input = input("Date: ").rstrip().lstrip()

            if "/" in _input:
                date = _input.split("/")
                day, month, year = date[1], date[0], date[2]

                if int(month) > 12 or int(day) > 31:
                    continue

                print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
            elif "," in _input:
                date = _input.split()
                day, month, year = date[1].replace(",", ""), date[0], date[2]

                if int(day) > 31:
                    continue

                print(f"{year}-{months[month].zfill(2)}-{day.zfill(2)}")
            else:
                continue
        except:
            continue
        else:
            break

main()
