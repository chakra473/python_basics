def function(x1, y1, z):
    if z == "+":
        return x1 + y1
    elif z == "-":
        return x1 - y1
    elif z == "*":
        return x1 * y1
    elif z == "/":
        return x1 / y1
    elif z == "&":
        return x1 & y1
    elif z == "|":
        return x1 | y1
    elif z == "^":
        return x1 ^ y1
    elif z == "<<":
        return x1 << y1
    elif z == ">>":
        return x1 >> y1


if __name__ == "__main__":

    x = 10
    y = 12
    a = function(x, y, "+")
    b = function(x, y, "-")
    c = function(x, y, "*")
    d = function(x, y, "/")
    e = function(x, y, "&")
    f = function(x, y, "|")
    g = function(x, y, "^")
    h = function(x, y, "<<")
    i = function(x, y, ">>")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
