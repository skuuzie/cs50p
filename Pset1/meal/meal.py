def main():

    inp = input('What time is it? ')
    time = convert(inp)

    if time >= 7 and time <= 8:
        print('breakfast time')
    elif time >= 12 and time <= 13:
        print('lunch time')
    elif time >= 18 and time <= 19:
        print('dinner time')

def convert(time):

    if ' ' in time:
        pre_time = time.split(' ')
        time = pre_time[0].split(':')
        indicator = pre_time[1]
        hour = int(time[0])

        if indicator == 'p.m.':
            if hour < 12:
                time[0] = hour + 12
    else:
        time = time.split(':')

    if time[1] == '00':
        return float(time[0])

    hour = time[0]
    minute = int(time[1]) / 60

    if minute < 1:
        minute = str(minute).split('.')[-1]

    return float(f'{hour}.{minute}')


if __name__ == "__main__":
    main()
