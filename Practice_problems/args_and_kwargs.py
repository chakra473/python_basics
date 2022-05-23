def my_func(*args):  # * is used to pass the desired number of arguments to the function.
    print(args)


def my_func1(**kwargs):  # **  represents keyword arguments, suggesting that this format uses keyword-based Python
    # dictionaries
    print(kwargs.values())


if __name__ == "__main__":
    my_func(1, 2, 3, 4, 5, 3.14, "hello", True)
    my_func1(name="abhi", location="odisha", age=22)
    my_func1(name="chakra", loation="chennai", age=23)
