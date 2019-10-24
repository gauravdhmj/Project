# number = "9,223,372,545,876,987,567"
# CleanedNumber = ''
#
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         CleanedNumber += number[i]
# USE OF AUGMENTED ASSIGNMENT
# NewNumber = int(CleanedNumber)
# print("the new number is {}".format(NewNumber))

# DIFFERENT OPERATORS AND THEIR AUGMENTED ASSIGNMENT

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x //= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

greeting = "Good "
greeting += "morning "
print(greeting)

greeting *= 5
print(greeting)

# += -= *= /= %= **= <<= >>= &= ^= |=