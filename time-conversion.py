
def timeConversion(s):
    hour = int(s[:2])
    am_or_pm = s[8:]
    if am_or_pm == 'PM':
        if hour != 12:
            hour = str(hour + 12)
    if am_or_pm == 'AM':
        if hour == 12:
            hour = 0
    hour = (str(hour).zfill(2))
    return f'{hour}{s[2:-2]}'


if __name__ == '__main__':

    s = input()
    print(timeConversion(s))
