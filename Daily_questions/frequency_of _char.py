def frequency_char(x):
    all_freq = {}

    for i in x:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    return ("Count of all characters in Geeks forGeeks is :\n "
            + str(all_freq))


if __name__ == "__main__":
    print(frequency_char("hello world this is program to find frequency of this string"))
