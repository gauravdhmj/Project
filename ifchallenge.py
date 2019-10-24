name = input("What is your name?\n")
age = int(input("What is your age?\n"))

if 18 <= age <= 38:
    print("{},You are invited to enjoy the holiday".format(name))
elif age < 18:
    print("{},You can surely enjoy the holidays after {} years ".format(name, 18 - age))
else:
    print("you missed the chance")