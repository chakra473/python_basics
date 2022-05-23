
def un_ordered_list(word):
    file_path = open("un_ordered_file.txt", "r")
    data = file_path.read()
    data_into_list = data.split(" ")
    for i in data_into_list:
        if i == word:
            data_into_list.remove(word)
            break
        else:
            data_into_list.append(word)
    # printing the data
    print(data_into_list)
    file_path.close()


print(un_ordered_list("hello"))
