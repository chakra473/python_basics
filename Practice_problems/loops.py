def for_loop(res):
    for m in range(1, 10 + 1):
        res += m
        print(res)


def while_loop(k):
    while k < 5:
        print(k)
        k += 1


if __name__ == "__main__":
    j = 0
    i = 0
    for_loop(i)
    while_loop(j)
