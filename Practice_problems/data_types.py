def data_type_fun(a, b, c, d, e, f, g, h, i, j, k, l1, m, n, o):
    """
    :param a:int input
    :param b:float input
    :param c:string input
    :param d:complex num input
    :param e:range input
    :param f:tuple input
    :param g:list input
    :param h:set input
    :param i:dictionary input
    :param j:bool input
    :param k:frozenset input
    :param l1:bytes input
    :param m:bytes_array input
    :param n:memory_view input
    :param o:none
    :return: void
    """
    print(type(a))  # prints data type of that variable
    print(a)  # prints a
    print(type(b))  # prints data type of that variable
    print(b)  # prints b
    print(type(c))  # prints data type of that variable
    print(c)  # prints c
    print(type(d))  # prints data type of that variable
    print(d)  # prints d
    print(type(e))  # prints data type of that variable
    print(e)  # prints e
    print(type(f))  # prints data type of that variable
    print(f)  # prints f
    print(type(g))  # prints data type of that variable
    print(g)  # prints g
    print(type(h))  # prints data type of that variable
    print(h)  # prints h
    print(type(i))  # prints data type of that variable
    print(i)  # prints i
    print(type(j))  # prints data type of that variable
    print(j)  # prints j
    print(type(k))  # prints data type of that variable
    print(k)  # prints k
    print(type(l1))  # prints data type of that variable
    print(l1)  # prints l
    print(type(m))  # prints data type of that variable
    print(m)  # prints m
    print(type(n))  # prints data type of that variable
    print(n)  # prints n
    print(type(o))  # prints data type of that variable
    print(o)  # prints o


if __name__ == "__main__":  # defining main function
    int_type = 25  # initializing variable
    float_type = 3.14  # initializing variable
    string_type = "Hello World"  # initializing variable
    complex_type = 1j  # initializing variable
    range_type = range(6)  # initializing variable
    tuple_type = ("apple", "banana", "cherry")  # initializing variable
    list_type = ["VIRAT", "ROHIT", "RAHUL"]  # initializing variable
    set_type = {"ROLLS ROYCE", "BMW", "PORSCHE", "FORD"}  # initializing variable
    dict_type = {"name": "MARSH", "nation": "AUSTRALIA"}  # initializing variable
    bool_type = True  # initializing variable
    frozenset_type = frozenset({"apple", "banana", "cherry"})  # initializing variable
    bytes_type = b"Hello"  # initializing variable
    bytearray_type = bytearray(5)  # initializing variable
    memory_view_type = memoryview(bytes(5))  # initializing variable
    none_type = None  # initializing variable
    data_type_fun(int_type, float_type, string_type, complex_type, range_type, tuple_type, dict_type, list_type,
                  set_type, bool_type, frozenset_type, bytes_type, bytearray_type, memory_view_type,
                  none_type)  # calling function by passing multiple arguments
