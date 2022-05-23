import random


class Coupon:

    @staticmethod
    def get_promo_code(num_chars, num):
        j = 0
        x = open("promo_code.txt", "a")
        while j < num:
            code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            code = ''
            for i in range(0, num_chars):
                slice_start = random.randint(0, len(code_chars) - 1)
                code += code_chars[slice_start]
            x.write(code)
            x.write("\n")
            print(code)
            j += 1
        x.close()


if __name__ == "__main__":
    Coupon.get_promo_code(10, 10)
    # print(random.randrange(1,3))
