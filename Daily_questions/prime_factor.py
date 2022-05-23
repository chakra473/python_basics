def prime_factor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            isprime = 1
            for j in range(2, (i // 2 + 1)):
                if i % j == 0:
                    isprime = 0
                    break

            if isprime == 1:
                print(f" %d is a Prime Factor of a Given Number %d" % (i, number))


if __name__ == '__main__':
    number1 = input("enter the number: ")
    prime_factor(number1)