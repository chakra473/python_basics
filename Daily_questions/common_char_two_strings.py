def common_char(x, y):
    a = list(set(x) & set(y))
    # b = []
    # for i in a:
    #     b.append(i)
    return a


if __name__ == '__main__':
    x1 = input("enter the first string: ")
    y1 = input("enter the second string: ")
    print(common_char(x1, y1))
