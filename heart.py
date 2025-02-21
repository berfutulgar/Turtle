import math
from turtle import *

def heart_a(a):
    return 15 * math.sin(a) ** 3

def heart_b(a):
    return 11.8 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 *a)

speed(0)
bgcolor("black")

for i in range(10000):
    x = heart_a(i) * 20
    y = heart_b(i) * 20
    goto(x, y)
    for j in range(3):
        goto(x, 0)
        color("red")

done()