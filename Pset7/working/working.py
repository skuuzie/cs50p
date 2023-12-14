import re
import sys

time_regex = r"^[0-9]{1,2}?(:[0-9]{2})? (AM|PM) to [0-9]{1,2}?(:[0-9]{2})? (AM|PM)$"


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(time_regex, s)

    if not match:
        raise ValueError("Invalid time format.")

    time_from, time_to = match[0].split(" to ")

    from_hour = "0"
    from_minute = "00"
    to_hour = "0"
    to_minute = "00"

    if ":" in time_from:
        if int(time_from.split(":")[-1][:2]) > 59:
            raise ValueError("Invalid time format.")

    if ":" in time_to:
        if int(time_to.split(":")[-1][:2]) > 59:
            raise ValueError("Invalid time format.")

    # from
    from_indicator = time_from[-2:]
    from_time, _ = time_from.split(" ")

    if ":" not in from_time:
        if from_indicator == "AM":
            from_hour = from_time
        if from_indicator == "PM":
            from_hour = str(int(from_time) + 12)
    else:
        _from_hour, from_minute = from_time.split(":")
        if from_indicator == "AM":
            from_hour = _from_hour
        if from_indicator == "PM":
            from_hour = str(int(_from_hour) + 12)

    # to
    to_indicator = time_to[-2:]
    to_time, _ = time_to.split(" ")

    if ":" not in to_time:
        if to_indicator == "AM":
            to_hour = to_time
        if to_indicator == "PM":
            to_hour = str(int(to_time) + 12)
    else:
        _to_hour, to_minute = to_time.split(":")
        if to_indicator == "AM":
            to_hour = _to_hour
        if to_indicator == "PM":
            to_hour = str(int(_to_hour) + 12)

    if from_hour == "12":
        from_hour = "0"
    if to_hour == "24":
        to_hour = "12"

    return f"{from_hour.zfill(2)}:{from_minute} to {to_hour.zfill(2)}:{to_minute}"


if __name__ == "__main__":
    main()
