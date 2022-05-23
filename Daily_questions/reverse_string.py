def reverse_str(arr):
    """

    :param arr: input the string
    :return: reversed string
    """
    return arr[::-1]


# Function to reverse words of string

def rev_sentence(sentence):
    """

    :param sentence:input the string
    :return: reversed string
    """
    # first split the string into words
    words = sentence.split(' ')

    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    # finally return the joined string
    return reverse_sentence[::-1], reverse_sentence


def reverse_word(input_string):
    """

    :param input_string:input the string
    :return:reversed string
    """
    new_list = []

    for i in range(len(input_string)):
        if input_string[i] != " ":
            new_list.append(input_string[i])

        else:
            while len(new_list) > 0:
                print(new_list[-1], end="")
                new_list.pop()
            print(end=" ")

    while len(new_list) > 0:
        print(new_list[-1], end="")
        new_list.pop()


if __name__ == '__main__':
    str1 = "hello world"
    print(reverse_str(str1))
    print(rev_sentence(str1))
