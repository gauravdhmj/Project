name = input("please enter your name:")
age = input("How old are you, {0}".format(name))
age = int(input("how old are you, {0}".format(name)))
print(age)
# USE OF IF SYNTAX
if age >= 18:
    print("you are old enough to vote")
    print("please put an x in the ballot box")
else:
    print("please come back after {} years".format(18 - age))

print("Please guess a number between 1 and 10:")
guess = int(input())

# Method 1

if guess < 5:
    print("Please guess a higher number")
    guess = int(input())
    if guess == 5:
        print("Well done ,you guessed it correctly")
    else:
        print("you have not guessed correctly")
elif guess > 5:
    print("Please guess a lower number")
    guess = int(input())
    if guess == 5:
        print("Well done ,you guessed it correctly")
    else:
        print("you have not guessed correctly")
else:
    print("You got it right the first time")

# Method 2

if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done ,you guessed it correctly")
    else:
        print("you have not guessed correctly")
else:
    print("You got it right the first time")

# USE OF AND and OR

age = int(input("How old are you?"))

# if (age>=16 and age<=65):
if (16 <= age <= 65):
    print("Have a good day at work")

if (age < 16) or (age > 66):
    print("Enjoy your meal at work")
else:
    print("have a good day at work")

x = "false"
if x:
    print("x is true")

print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list[]: {4}
empty tuple(): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False,bool(None),bool(0),bool(0.0),bool([]),bool(()),bool(''),bool(""),bool({}) ))

x = input("Please enter some text")
if x:
    print('You entered "{}" '.format(x) )
else:
    print("you did not enter anything")


# USE OF NOT KEYWORD

print(not True)
print(not False)

# EXAMPLE OF NOT KEYWORD

age = int(input("how old are you,"))
if not(age <= 18):
    print("you are old enough to vote")
    print("please put an x in the ballot box")
else:
    print("please come back after {} years".format(18 - age))

# USE OF IN KEYWORD(DONE IN PREVIOUS VIDEOS)

parrot = "Norwegnian blue"

letter = input("enter any character\n")
if letter in parrot:
    print("give me the letter {} lol".format(letter))
else:
    print("apne pass rakh ise")


# USE OF NOT IN KEYWORD

parrot = "Norwegnian blue"

letter = input("enter any character\n")
if letter not in parrot:
    print("apne pass rakh ise")
else:
    print("give me the letter {} lol".format(letter))
