print("Enter a year to check whether it is leap year or not")
n = int(input())
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(n, "it is a Leap Year!!")
else:
    print(n, "it is not a Leap year")