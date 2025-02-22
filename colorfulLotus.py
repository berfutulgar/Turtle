from turtle import *
import colorsys as cs

tracer(100)
pensize(2)
bgcolor("black")
h = 0

for i in range(500):
    c = cs.hsv_to_rgb(h, 1, 1)
    h += 0.008
    color(c)
    rt(119)
    circle(-i * 0.4, 90)
    right(91)
    circle(-i * 0.4, 90)

done()