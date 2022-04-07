import turtle
import time
import random

print("Remember to maximize the turtle window. ")

width = 30
x = 200
y = 300

t_gallow = turtle.Pen()
t_gallow.hideturtle()
t_gallow.up()
t_gallow.forward(200)
t_gallow.left(90)
t_gallow.forward(300)
t_gallow.right(90)
t_gallow.down()
t_gallow.forward(0.5 * (300 + width))
t_gallow.right(45)
t_gallow.forward(2 ** 0.5 * (150 - width))
t_gallow.right(45)
t_gallow.forward(600 - (150 - width))
t_gallow.right(90)
t_gallow.forward(0.5 * (400 - width))
t_gallow.left(90)
t_gallow.forward(width)
t_gallow.left(90)
t_gallow.forward(400)
t_gallow.left(90)
t_gallow.forward(width)
t_gallow.left(90)
t_gallow.forward(0.5 * (400 - width))
t_gallow.right(90)
t_gallow.forward(600)
t_gallow.forward(width)
t_gallow.left(90)
t_gallow.forward(0.5 * (600 + width))
t_gallow.left(90)
t_gallow.forward(width)
t_gallow.left(90)
t_gallow.up()


x = random.randint(1,15)



