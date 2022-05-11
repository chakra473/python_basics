import random
print("enter the number of times to flip a coin")
x = int(input())
i = 1
tail = 1
head = 2
t = 0
h = 0
while i <= x:
    y = random.randint(1, 2)
    if y == tail:
        t += 1
    else:
        h += 1
    i += 1
p1 = h / x * 100
p2 = t / x * 100
myOrder0 = "no of heads  is {0}"
myOrder01 = "no of tails is {0}"
myOrder = "heads percentage is {0} %"
myOrder1 = "tails percentage is {0} %"
print(myOrder0.format(h))
print(myOrder01.format(t))
print(myOrder.format(p1))
print(myOrder1.format(p2))
