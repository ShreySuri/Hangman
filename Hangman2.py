print("Welcome to Hangman. The rules of this game can be found in the README file. Note that if a word contains the same letter multiple types, you need to guess that letter multiple times.")
print("")

a = input(print("If you would like a hint, type 'list' to pull up the word list."))
a = str(a)
a = a.upper()
if a == "LIST":
    print("Units are categorized by what they quantify")
    print("")
    print("Volume            Distance     Mass")
    print("")
    print("ounce             inch         gram")
    print("cup               foot         ounce")
    print("pint              yard         pound")
    print("quart             meter        ton")
    print("liter             mile"
    print("gallon")
    print("")
    print("Hope this helps")
else:
    print("I didn't understand. No helpful hints for you!")
