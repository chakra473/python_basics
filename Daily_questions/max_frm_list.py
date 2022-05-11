# Python program to find the largest
# number in a list

def my_max(list_1):
    max_list = list_1[0]

    for x in list_1:
        if x > max_list:
            max_list = x

    return max_list


if __name__ == "__main__":
    list1 = [10, 20, 4, 45, 99]
    print("Largest element is:", my_max(list1))
