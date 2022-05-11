# Python program to Find day of
# the week for a given date
import datetime
import calendar


def find_day(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return calendar.day_name[born]


def day_of_week(day, month, year):
    y = year - (14 - month) // 12
    x = y + (y // 4) - (y // 100) + (y // 400)
    m = month + 12 * ((14 - month) // 12) - 2
    d = (day + x + 31 * m // 12) % 7
    if d == 0:
        return "SUNDAY"
    elif d == 1:
        return "MONDAY"
    elif d == 2:
        return "TUESDAY"
    elif d == 3:
        return "WEDNESDAY"
    elif d == 4:
        return "THURSDAY"
    elif d == 5:
        return "FRIDAY"
    elif d == 6:
        return "SATURDAY"


class TestClass:

    def test_one(self):
        x = day_of_week(10, 5, 2022)
        y = find_day('10 5 2022')
        assert x == y.upper()  # testing whether Gregorian calendar formula is correct or not with date time and
        # calender module
