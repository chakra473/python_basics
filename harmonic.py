n = int(input("enter the number to calculate harmonic\n"))
num = 0
res = 0
i = 1
while i <= n:
    res = float(1 / i)
    num = float(num + res)
    i += 1
print("the ", n, "th harmonic value is ", num)
