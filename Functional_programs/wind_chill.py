# importing pow function from math module
from math import pow


def wind_chill(t, v):
    """

    :param t: temperature in fahrenheit
    :param v: wind speed in miles per hour
    :return:
    """
    if t <= 50 and 3 <= v <= 120:
        w = 35.74 + (0.6215 * t) + ((0.4275 * t - 35.75) * (pow(v, 0.16)))
        print(f"the wind chill is %.2f" % w + u"\N{DEGREE SIGN}F")
    else:
        print("invalid input")


if __name__ == "__main__":
    temp = int(input("enter the temperature in fahrenheit: "))
    speed = int(input("enter the wind speed in miles per hour: "))
    wind_chill(temp, speed)
