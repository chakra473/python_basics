def count_vowels(x):
    """

    :param x:
    :return:
    """
    vowels_count = 0
    consonants_count = 0
    for i in x:
        if (i == "a" or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
                i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels_count += 1
        elif i != " " and i != "@" and i != "!" and i != "$" and i != "/":
            consonants_count += 1

    return vowels_count, consonants_count


a, b = count_vowels("hello world!!")
print(f"number of vowels in the given string is {a}")
print(f"number of consonants in the given string is {b}")
