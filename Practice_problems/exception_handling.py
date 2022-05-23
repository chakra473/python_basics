import array

try:
    r = 1/0
    array_data = array.array('i', [1, 2, 3, 4, "hi"])
    for i in array_data:
        print(i)
except TypeError as err:
    print(err)
except ZeroDivisionError as err1:
    print(err1)
