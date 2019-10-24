# USE OF FOR LOOP

for i in range(1,20):
    print("i is now {}".format(i))

# USE OF len KEYWORD IN FOR LOOP

number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    print(number[i])
print("\n")

# USE OF IN KEYWORD IN FOR LOOP

for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i],end='')
print("\n")
# CONVERTING INTEGER INTO STRING AND THE TO INTEGER

# METHOD 1

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range (0, len (number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

#  METHOD 2

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin'","no more", "a stiff", "bereft of life"]:
    print("This parrot is "+ state)
    print("This parrot is {}".format(state))

for i in range(0, 100, 5):
    print("i is {} ".format(i))

# NESTED FOR LOOP

for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j), end='\t')
    # print("================")
    print('\n')

for i in range(0,101):
    if (i%7 == 0):
        print(i,end='\n')