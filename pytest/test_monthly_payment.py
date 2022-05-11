def monthly_pay(year, principle, interest):
    r = interest / (12 * 100)
    n = 12 * year
    payment = principle * r / (1 - ((1 + r) ** (-n)))
    return payment


class TestClass:

    def test_one(self):
        y = 10
        p = 100000
        i = 20
        x = monthly_pay(y, p, i)
        assert x < p
