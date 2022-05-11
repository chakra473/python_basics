# defining euclidean function to calculate euclidean distance from the point (x, y) to the origin (0, 0).


def euclidean_dist(x, y):
    dist = (x * x + y * y)**0.5
    return dist


if __name__ == "__main__":
    input1 = int(input("enter the value of x: "))
    input2 = int(input("enter the value of y: "))
    res = euclidean_dist(input1, input2)
    print("euclidean distance from the point (" + str(input1) + ", " + str(input2) + " )" + "to the origin (0, 0)", res)
