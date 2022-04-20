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
t_gallow.forward(650 - (150 - width))
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
t_gallow.forward(650)
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
t_gallow.forward(145)
t_gallow.forward(2 ** 0.5 * width)
t_gallow.left(90)
t_gallow.down()


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
underscore.right(180)
underscore.forward(50)
underscore.left(90)
underscore.forward(15)
underscore.right(90)

incorrect = 0
counter = 0
place_mark = 0
correct = False
print(word)

while incorrect < 9 and counter < letters:
    guess = input(print("Please guess a letter. "))
    guess = guess.lower()
    for j in range (0,letters):
        if guess == word[j]:
            correct = True
            counter = counter + 1
            underscore.forward(125*j)
        if guess == "a" and correct == True:
            underscore.down()
            underscore.left(73)
            underscore.forward(130.5)
            underscore.right(146)
            underscore.forward(130.5)
            underscore.right(180)
            underscore.forward(70)
            underscore.left(73)
            underscore.forward(37)
            underscore.hideturtle()           
            underscore.left(73)
            underscore.forward(70)
            underscore.right(73)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "b" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(42)
            for i in range(1,181):
                underscore.forward(0.55)
                underscore.right(1)
            underscore.forward(42)
            underscore.right(180)
            underscore.forward(42)
            for i in range(1,181):
                underscore.forward(0.55)
                underscore.right(1)
            underscore.forward(42)
            underscore.right(180)
            underscore.forward(42)
            for i in range(1,181):
                underscore.left(1)
                underscore.forward(0.55)
            underscore.left(180)
            for i in range (1,181):
                underscore.left(1)
                underscore.forward(0.55)
            underscore.forward(42)
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "c" and correct == True:
            underscore.up()
            underscore.left(90)
            underscore.forward(45)
            underscore.right(90)
            underscore.forward(75)
            underscore.right(90)
            underscore.down()
            for i in range(1,181):
                underscore.forward(0.65)
                underscore.right(1)
            underscore.forward(40)
            for i in range(1,181):
                underscore.forward(0.65)
                underscore.right(1)
            underscore.up()
            underscore.forward(40)
            underscore.forward(45)
            underscore.right(90)
            underscore.forward(75)
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "d" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            for i in range (1,180):
                underscore.forward(1.1)
                underscore.right(1)
            underscore.right(180)
            for i in range (1,180):
                underscore.left(1)
                underscore.forward(1.1)
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "e" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(75)
            underscore.right(180)
            underscore.forward(75)
            underscore.left(90)
            underscore.forward(62)
            underscore.left(90)
            underscore.forward(50)
            underscore.right(180)
            underscore.forward(50)
            underscore.left(90)
            underscore.forward(63)
            underscore.left(90)
            underscore.forward(75)
            underscore.right(180)
            underscore.forward(75)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "f" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(75)
            underscore.right(180)
            underscore.forward(75)
            underscore.left(90)
            underscore.forward(62)
            underscore.left(90)
            underscore.forward(50)
            underscore.right(180)
            underscore.forward(50)
            underscore.left(90)
            underscore.forward(63)
            underscore.right(90)
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "g" and correct == True:
            underscore.left(90)
            underscore.up()
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(50)
            underscore.right(180)
            underscore.down()
            underscore.forward(12)
            for i in range(1,91):
                underscore.forward(0.65)
                underscore.left(1)
            underscore.forward(50)
            for i in range(1,181):
                underscore.forward(0.65)
                underscore.left(1)
            underscore.forward(30)
            underscore.left(90)
            underscore.forward(50)
            underscore.right(180)
            underscore.forward(50)
            underscore.right(90)
            underscore.forward(30)
            for i in range(1,181):
                underscore.right(1)
                underscore.forward(0.65)
                underscore.forward(50)
            for i in range(1,91):
                underscore.right(1)
                underscore.forward(0.65)
            underscore.up()
            underscore.right(180)
            underscore.forward(38)
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "h" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(180)
            underscore.forward(62)
            underscore.left(90)
            underscore.forward(75)
            underscore.left(90)
            underscore.forward(62)
            underscore.right(180)
            underscore.forward(125)
            underscore.right(90)
            underscore.up()
            underscore.forward(75)
            underscore.forward(125*j)
        if guess == "i" and correct == True:
            underscore.forward(75)
            underscore.right(180)
            underscore.forward(37.5)
            underscore.right(90)
            underscore.forward(125)
            underscore.left(90)
            underscore.up()
            underscore.forward(37.5)
            underscore.right(180)
            underscore.down()
            underscore.forward(75)
            underscore.right(90)
            underscore.up()
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(75)
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "j" and correct == True:
            underscore.left(90)
            underscore.up()
            underscore.forward(125)
            underscore.right(90)
            underscore.down()
            underscore.forward(75)
            underscore.right(180)
            underscore.forward(25)
            underscore.left(90)
            underscore.forward(y)
            for i in range (1,91):
                underscore.forward(x)
                underscore.right(2)
            underscore.right(180)
            for i in range (1,91):
                underscore.left(2)
                underscore.forward(x)
            underscore.forward(y)
            underscore.left(90)
            underscore.forward(50)
            underscore.left(90)
            underscore.up()
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(125*j)
            underscore.right(90)
        if guess == "k" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(180)
            underscore.forward(62)
            underscore.left(130)
            underscore.forward(97)
            underscore.right(180)
            underscore.forward(97)
            underscore.left(100)
            underscore.forward(97)
            underscore.right(180)
            underscore.forward(97)
            underscore.left(130)
            underscore.forward(63)
            underscore.right(90)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "l" and correct == True:
            underscore.up()
            underscore.left(90)
            underscore.forward(125)
            underscore.right(180)
            underscore.down()
            underscore.forward(125)
            underscore.left(90)
            underscore.forward(75)
            underscore.right(180)
            underscore.up()
            underscore.forward(75)
            underscore.forward(125*i)
            underscore.right(180)
        if guess == "m" and correct == True:
            underscore.left(80)
            underscore.forward(125)
            underscore.right(160)
            underscore.forward(90)
            underscore.left(160)
            underscore.forward(90)
            underscore.right(160)
            underscore.forward(125)
            underscore.right(180)
            underscore.forward(125)
            underscore.left(160)
            underscore.forward(90)
            underscore.right(160)
            underscore.forward(90)
            underscore.left(160)
            underscore.forward(125)
            underscore.right(80)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "n" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(149)
            underscore.forward(146)
            underscore.left(149)
            underscore.forward(125)
            underscore.right(180)
            underscore.forward(125)
            underscore.right(149)
            underscore.forward(146)
            underscore.left(149)
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "o" and correct == True:
            underscore.left(90)
            underscore.up()
            underscore.forward(37)
            underscore.down()
            for i in range (0,2):
                underscore.forward(50)
                for i in range (1,181):
                    underscore.forward(0.65)
                    underscore.right(1)
            underscore.right(180)
            underscore.up()
            underscore.forward(37)
            underscore.right(90)
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "p" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(42)
            for i in range(1,181):
                underscore.forward(0.55)
                underscore.right(1)
            underscore.forward(42)
            underscore.right(180)
            underscore.forward(42)
            for i in range (1,181):
                underscore.left(1)
                underscore.forward(0.55)
            underscore.forward(42)
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "q" and correct == True:
            underscore.left(90)
            underscore.up()
            underscore.forward(37)
            underscore.down()
            underscore.forward(50)
            for i in range (1,181):
                underscore.forward(0.65)
                underscore.right(1)
            underscore.forward(50)
            for i in range (1,46):
                underscore.forward(0.65)
                underscore.right(1)
            underscore.right(100)
            underscore.up()
            underscore.forward(30)
            underscore.right(180)
            underscore.down()
            underscore.forward(45)
            underscore.right(180)
            underscore.up()
            underscore.forward(15)
            underscore.left(100)
            underscore.down()
            for i in range (1,136):
                underscore.forward(0.65)
                underscore.right(1)
            underscore.right(180)
            underscore.up()
            underscore.forward(37)
            underscore.right(90)
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "r" and correct == True:
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.forward(42)
            for i in range(1,181):
                underscore.forward(0.55)
                underscore.right(1)
            underscore.forward(42)
            underscore.left(140)
            underscore.forward(95)
            underscore.right(180)
            underscore.forward(95)
            underscore.right(140)
            underscore.forward(42)
            for i in range (1,181):
                underscore.left(1)
                underscore.forward(0.55)
            underscore.forward(42)
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "s" and correct == True:
            underscore.forward(31)
            underscore.forward(12)
            for i in range (1,181):
                underscore.forward(0.55)
                underscore.left(1)
            underscore.forward(12)
            for i in range (1,181):
                underscore.forward(0.55)
                underscore.right(1)
            underscore.forward(12)
            underscore.forward(31)
            underscore.right(180)
            underscore.forward(31)
            underscore.forward(12)
            for i in range (1,181):
                underscore.left(1)
                underscore.forward(0.55)
            underscore.forward(12)
            for i in range (1,181):
                underscore.right(1)
                underscore.forward(0.55)
            underscore.forward(12)
            underscore.forward(31)
            underscore.up()
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "t" and correct == True:
            underscore.left(90)
            underscore.up()
            underscore.forward(125)
            underscore.right(90)
            underscore.down()
            underscore.forward(75)
            underscore.right(180)
            underscore.forward(37.5)
            underscore.left(90)
            underscore.forward(125)
            underscore.right(90)
            underscore.up()
            underscore.forward(37.5)
            underscore.forward(125*j)
            underscore.right(180)
        if guess == "u" and correct == True:
            underscore.left(90)
            underscore.forward(40)
            underscore.forward(85)
            underscore.right(180)
            underscore.forward(85)
            for i in range (1,181):
                underscore.forward(0.65)
                underscore.left(1)
            underscore.forward(85)
    if correct == False:
        incorrect = incorrect + 1
        if incorrect == 1:
            t_gallow.width(3)
            t_gallow.pencolor("tan")
            t_gallow.forward(100)
        if incorrect == 2:
            t_gallow.width(1)
            t_gallow.pencolor("black")
            t_gallow.up()
            t_gallow.right(90)
            t_gallow.down()
            t_gallow.circle(50)
            t_gallow.left(90)
            t_gallow.up()
            t_gallow.forward(100)
        if incorrect == 3:
            t_gallow.down()
            t_gallow.forward(250)
        if incorrect == 4:
            t_gallow.right(180)
            t_gallow.forward(200)
            t_gallow.left(150)
            t_gallow.forward(150)
        if incorrect == 6:
            t_gallow.right(180)
            t_gallow.forward(150)
            t_gallow.right(120)
            t_gallow.forward(150)
        if incorrect == 7:
            t_gallow.right(180)
            t_gallow.forward(150)
            t_gallow.left(150)
            t_gallow.forward(200)
            t_gallow.right(30)
            t_gallow.forward(150)
        if incorrect == 8:
            t_gallow.right(180)
            t_gallow.forward(150)
            t_gallow.right(120)
            t_gallow.forward(150)
        if incorrect == 9:
            t_gallow.right(180)
            t_gallow.forward(150)
            t_gallow.right(30)
            t_gallow.up()
            t_gallow.forward(325)
            t_gallow.left(90)
            t_gallow.forward(25)
            t_gallow.left(135)
            t_gallow.down()
            t_gallow.forward(28.28)
            t_gallow.up()
            t_gallow.left(135)
            t_gallow.forward(20)
            t_gallow.left(135)
            t_gallow.down()
            t_gallow.forward(28.28)
            t_gallow.up()
            t_gallow.right(135)
            t_gallow.forward(20)
            t_gallow.right(90)
            t_gallow.forward(30)
            t_gallow.right(180)
            t_gallow.left(135)
            t_gallow.down()
            t_gallow.forward(28.28)
            t_gallow.up()
            t_gallow.left(135)
            t_gallow.forward(20)
            t_gallow.left(135)
            t_gallow.down()
            t_gallow.forward(28.28)
            t_gallow.up()
            t_gallow.left(45)
            t_gallow.forward(25)
            t_gallow.left(90)
            t_gallow.forward(30)
            t_gallow.right(180)
            t_gallow.down()
            t_gallow.forward(70)
        correct = False

if counter == letters:
    print("Congrats, you won! ")
if incorrect == 9:
    print("Sorry, you lost. ")
else:
    print("Error. ")

    



