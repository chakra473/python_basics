def funct(list1, k):
    for i in range(len(list1)):
        for j in range(1, len(list1)):
            num = list1[i] + list1[j]
            if num == k:
                return i, j


if __name__ == '__main__':
    list2 = [1, 5, 2, 7, 3, 10]
    k1 = 7
    print(funct(list2, k1))
