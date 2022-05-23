def binary_search_word(string_list, search_word):
    ls = sorted(string_list)
    left = 0
    right = len(string_list) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if search_word == ls[mid]:
            return mid

        if search_word > ls[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    file_path = open("un_ordered_file.txt", "r")
    data = file_path.read()
    list_item = data.split(" ")
    word = "hello"

    output = binary_search_word(list_item, word)
    print(output != -1)
