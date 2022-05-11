# importing square root function from math module
from math import sqrt


# defining quadratic function to find the roots of that equation
def quadratic(a, b, c):
    delta = (b * b) - (4 * a * c)

    x1 = ((-b + (sqrt(delta))) / (2 * a))

    x2 = ((-b - (sqrt(delta))) / (2 * a))

    print(f'The 2 roots of the equation are :\nx={x1}\nx={x2}')


if __name__ == "__main__":
    print("the equation a*x*x + b*x + c.")
    a1 = int(input("enter the value of a: "))
    b1 = int(input("enter the value of b: "))
    c1 = int(input("enter the value of c: "))
    print(f"The equation is {a1}*x*x + {b1}*x + {c1} ")
    quadratic(a1, b1, c1)
