import turtle
import random
import time

print("Remember to maximize the turtle window. ")

width = 25


t_gallow = turtle.Pen()

t_gallow.hideturtle()
t_gallow.forward(1)
t_gallow.up()
t_gallow.forward(200)
t_gallow.left(90)
t_gallow.forward(300)
t_gallow.right(90)
t_gallow.down()
t_gallow.fillcolor("brown")
t_gallow.begin_fill()
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
t_gallow.end_fill()
t_gallow.fillcolor("white")
t_gallow.begin_fill()
t_gallow.up()
t_gallow.forward(150)
t_gallow.forward(2 ** 0.5 * width)
t_gallow.right(45)
t_gallow.down()
t_gallow.forward(2 ** 0.5 * (150 - 2 * width))
t_gallow.left(135)
t_gallow.forward(150 - 2 * width)
t_gallow.left(90)
t_gallow.forward(150 - 2 * width)
time.sleep(0.2)
t_gallow.end_fill()
t_gallow.up()


x = random.randint(1,15)

if x == 1:
    word = ["o","u","n","c","e"]
    letters = 5
elif x == 2:
    word = ["c","u","p"]
    letters = 3
elif x == 3:
    word = ["p","i","n","t"]
    letters = 4
elif x == 4:
    word = ["q","u","a","r","t"]
    letters = 5
elif x == 5:
    word = ["l","i","t","e","r"]
    letters = 5
elif x == 6:
    word = ["g","a","l","l","o","n"]
    letters = 6
elif x == 7:
    word = ["i","n","c","h"]
    letters = 4
elif x == 8:
    word = ["f","o","o","t"]
    letters = 4
elif x == 9:
    word = ["y","a","r","d"]
    letters = 4
elif x == 10:
    word = ["m","e","t","e","r"]
    letters = 5
elif x == 11:
    word = ["m","i","l","e"]
    letters = 4
elif x == 12:
    word = ["g","r","a","m"]
    letters = 4
elif x == 13:
    word = ["o","u","n","c","e"]
    letters = 5
elif x == 14:
    word = ["p","o","u","n","d"]
    letters = 5
elif x == 15:
    word = ["t","o,","n"]
    letters = 3
else:
    print("Something went wrong. ")

underscore = turtle.Pen()
underscore.hideturtle()
underscore.up()
underscore.right(90)
underscore.forward(200)
underscore.right(90)
for i in range (0, letters):
    underscore.down()
    underscore.forward(75)
    underscore.up()
    underscore.forward(50)
    

    



