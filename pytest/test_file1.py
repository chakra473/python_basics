# content of test_class.py
class TestClass:
    check = True

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = TestClass()

        assert hasattr(x, "check")
