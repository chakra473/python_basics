def uc1_length(x1, y1, x2, y2):
    sum1 = ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))
    result = sum1 ** 0.5
    return result


def uc_2_check_lines(a1, b1, a2, b2):
    if a1 == a2:

        return b1 == b2

    else:

        len1 = b1 - a1
        len2 = b2 - a2
        return len1 == len2


def uc_3_compare_lines(l1, m1, l2, m2):
    if l1 == l2:
        comp = cmp(m1, m2)
        if comp == 0:
            return "Both line are equals"

        elif comp >= 0:
            return "Second line is Smaller than first"

        else:
            return "Second line is bigger than First"

    else:

        le1 = m1 - l1
        le2 = m2 - l2
        comp = cmp(le1, le2)
        if comp == 0:

            return "Both line are equals"

        elif comp >= 0:

            return "Second line is Smaller than first"

        else:

            return "Second line is bigger than First"


def cmp(a, b):
    return (a > b) - (a < b)


if __name__ == "__main__":
    print(uc1_length(10, 20, 5, 3))
    print(uc_2_check_lines(1, 2, 3, 4))
    print(uc_3_compare_lines(2, 14, 2, 14))
