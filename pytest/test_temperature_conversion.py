def temp_con(symbol, temp):
    try:
        if symbol == "F":
            f = (temp * 9 / 5) + 32
            return f
        elif symbol == "C":
            c = (temp - 32) * 5 / 9
            return c
        raise ValueError("invalid number")
    except ValueError as err:
        print(err)


class TestClass:

    def test_one(self):  # test case for converting temp from celsius to fahrenheit
        s = "F"
        c = 24           # c is temperature in celsius
        x = temp_con(s, c)
        assert 32 < x < 212

    def test_two(self):  # test case for converting temp from fahrenheit to celsius
        s = "C"
        f = 130         # f is temperature in fahrenheit
        x = temp_con(s, f)
        assert 0 < x < 100
