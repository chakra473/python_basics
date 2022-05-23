def prime_range(lower, upper):
    prime_list = []
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
                print(num)


if __name__ == '__main__':
    lower1 = 100
    upper1 = 200
    print(prime_range(lower1, upper1))
