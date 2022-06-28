import turtle
import random
import time


def listToString(s): 
    str1 = ""  
    for ele in s: 
        str1 += ele    
    return str1 

print("Remember to maximize the turtle window. ")
print("")

width = 30

t_gallow = turtle.Pen()

t_gallow.hideturtle()

time.sleep(5)

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

game = True
all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
guesses = []
known_word = []
for i in range (0, letters):
    string = "_ "
    known_word.append(string)
incorrect = 0
correct_count = 0
total_guess_count = 0
total_guess = []

print(listToString(known_word))
print("")

while game == True:
    
    valid_guess = False
    
    while valid_guess == False:
        
        guess = input(print("Please guess a letter. If you would like a word library, type 'library'."))
        guess = guess.lower()

        for i in range (0, 26):
            if all_letters[i] == guess:
                valid_guess = True
            else:
                toggle = True

        if valid_guess == True and total_guess_count > 0:
            for i in  range (0, total_guess_count):
                if total_guess[i] == guess:
                    print("")
                    print("You have already guessed this letter. Please choose a different one.")
                    print("")
                    valid_guess = False
                else:
                    toggle = False
        else:
            toggle = True

                
        if guess == "library":
            print("")
            print("cup")
            print("ton")
            print("foot")
            print("gram")
            print("inch")
            print("mile")
            print("pint")
            print("yard")
            print("liter")
            print("meter")
            print("ounce")
            print("pound")
            print("quart")
            print("gallon")
            print("")
        else:
            toggle = False

    total_guess.append(guess)
    total_guess_count = total_guess_count + 1


    correct = False
    
    for i in range (0, letters):
        if word[i] == guess:
            string = "%s " % guess
            known_word[i] = string
            correct = True
        else:
            toggle = True

    if correct == True:
        str_known_word = listToString(known_word)
        full_str = "Word: %s" % str_known_word
        print(full_str)
        print("")
        correct_count = correct_count + 1
        if correct_count == letters:
            game = False
            win = True
        else:
            toggle = True
    else:
        string = "%s " % guess
        guesses.append(string)
        str_guesses = listToString(guesses)
        full_str = "Incorrect Guesses: %s" % str_guesses
        print(full_str)
        print("")
        incorrect = incorrect + 1

        if incorrect == 1:
            t_gallow.width(3)
            t_gallow.pencolor("tan")
            t_gallow.forward(100)
        elif incorrect == 2:
            t_gallow.width(1)
            t_gallow.pencolor("black")
            t_gallow.up()
            t_gallow.right(90)
            t_gallow.down()
            t_gallow.circle(50)
            t_gallow.left(90)
            t_gallow.up()
            t_gallow.forward(100)
        elif incorrect == 3:
            t_gallow.down()
            t_gallow.forward(250)
        elif incorrect == 4:
            t_gallow.right(180)
            t_gallow.forward(200)
            t_gallow.left(150)
            t_gallow.forward(150)
        elif incorrect == 5:
            t_gallow.right(180)
            t_gallow.forward(150)
            t_gallow.right(120)
            t_gallow.forward(150)
        elif incorrect == 6:
            t_gallow.right(180)
            t_gallow.forward(150)
            t_gallow.left(150)
            t_gallow.forward(200)
            t_gallow.right(30)
            t_gallow.forward(150)
        elif incorrect == 7:
            t_gallow.right(180)
            t_gallow.forward(150)
            t_gallow.right(120)
            t_gallow.forward(150)
        elif incorrect == 8:
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

            game = False
            win = False
            
        else:
            print("Something went wrong.")


if win == True:
        print("Yay! You won! It took you %s guesses." % total_guess_count)
else:
    print("Oh no, the man has been hung. Give it another shot.")
    word = listToString(word)
    print("")
    print("The word was %s." % word)
            
        
        
               

