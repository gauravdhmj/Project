#  METHOD 1 TO CREATE SETS
# SETS ARE UNORDERED IN NATURE

# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" *40)

# METHOD 2 TO CREATE SETS

# wild_animals = set(["lion", "tiger" ,"panther", "elephant", "hare"])
# print(wild_animals)
# for animal in wild_animals:
#     print(animal)

# USE OF ADD COMMAND TO ADD ELENTS IN THE SET

# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# USE OF SET CONSTRUCTOR NECESSARY TO CREATE SETS

# empty_set = set()
# empty_set_2 = {}
# empty_set.add("a")
# empty_set_2.add("a")

# CREATING A SET USING RANGES AND TUPLES

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# OPERATION ON SETS
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))

# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))

# UNION COMMAND
# print(even.union(squares))
# print(len(even.union(squares)))
# print(even | squares)
# print(squares.union(even))

# print("-" * 40)

# INTERSECTION COMMAND
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#
# DIFFERENCE COMMAND
# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))

# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))

# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)

# difference update command
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# LOL
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# SYMMETRIC DIFFERENCE

# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(squares.symmetric_difference(even))

# REMOVING OR DISCARDING ELEMENTS FROM THE SET

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)   # no error, does nothing
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")

# SUBSET AND SUPERSET OF A SET

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")

#  FROZEN SET (IMMUTABLE SET)
# a frozen set is a set which can't be changed we can not add or remove elements from a frozen set .
# operations that can be performed on a frozen set are union ,intersection and difference.
# while we cannot perform operations like difference_update and symmetric_update
# even = frozenset(range(0, 100, 2))
#
# print(even)
# even.add(3)

# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

sampleText = "Python is a very powerful language"
x =""
vowel = "aeiou"
vowels = frozenset("aeiou")
vowels = {"a", "e", "i", "o", "u"}
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)
for i in range(0, len(sampleText)):
    if sampleText[i] not in vowel:
        x+=sampleText[i]

print(sorted(list(x)))