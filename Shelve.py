# pickle has several drawbacks related to storing the data into the file
# shelves are used to overcome that drawback
# shelves can be considered as a persistent dictionary which means it can have all dictionary operations performed on it
# shelve file is already opened in read and write format together

# import shelve
# errors in using with statement as with statement closes the file before we print the output
# with shelve.open('ShelfTest') as fruit:
#      fruit['orange'] = "a sweet, orange, citrus fruit"
#      fruit['apple'] = "good for making cider"
#      fruit['lemon'] = "a sour, yellow citrus fruit"
#      fruit['grape'] = "a small, sweet fruit growing in bunches"
#      fruit['lime'] = "a sour, green citrus fruit"
#
#      print(fruit["lemon"])
#      print(fruit["grape"])
# file is closed here
# print(fruit)
#
# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
# file is cosed so error is coming
# print(fruit["lemon"])
# print(fruit["grape"])

# print(fruit)
#
# without using with statement
# fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"
#
# print(fruit["lemon"])
# print(fruit["grape"])
# fruit.close()
#
# print(fruit)


# DIFFERENCE BETWEEN SHELVE AND DICTIONARY
# (shelves only accept strings as a key while a dictionary can accept any immutable key as a key)

# with shelve.open('ShelfTest') as fruit:
#      fruit = {"orange": "a sweet, orange, citrus fruit",
#               "apple": "good for making cider",
#               "lemon": "a sour, yellow citrus fruit",
#               "grape": "a small, sweet fruit growing in bunches",
#               "lime": "a sour, green citrus fruit"}
#
#      print(fruit["lemon"])
#      print(fruit["grape"])
#
# print(fruit)


# import shelve

# with shelve.open("bike") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engin_size"] = 250

# receiving the value from both the database

    # print(bike["engin_size"])
    # print(bike["engine_size"])
    # print(bike["colour"])
    #
    # del bike['engin_size']
    #
    # for key in bike:
    #     print(key)

    # print('=' * 40)

# Add or update any key  or value in the shelve file

# import shelve
#
# fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"
#
# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
# for i in fruit:
#     print(i + ":" + fruit[i])

# USE OF GET COMMAND to retrieve the data

# while True:
#     dict_key = input("Please enter the fruit: ")
#     if dict_key == "quit":
#         break
#
#     description = fruit.get(dict_key, "we don't have a " + dict_key)
#     print(description)
#
# fruit.close()

# print(fruit)
# USING OTHER METHOD (IN COMMAND)

# while True:
#     dict_key = input("Please enter the fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("we don't have a" + dict_key)

# ORDERING THE KEYS IN THE SHELVE

# ordered_keys = sorted(fruit.keys())
# for f in ordered_keys:
#     print(f + " : " + fruit[f])

# for v in fruit.values():
#     print(v)

# print(fruit.values())
# for f in fruit.items():
#     print(f)

# print(fruit.items())
# fruit.close()

# UPDATING SHELVES

import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# with shelve.open('recipes') as recipes:
with shelve.open('recipes', writeback=True) as recipes:

    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta" ] = pasta
    # recipes["soup"] = soup
    #
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    # the value is stored in the memory
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
    # recipes["soup"].append("croutons")
    recipes["soup"] = soup
    recipes.sync()
    soup.append("carrot")

for snack in recipes:
    print(snack, recipes[snack])
