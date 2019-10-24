ipaddress = input("Please enter an ip address: ")
print(ipaddress.count("."))

parrot_list = ["non pinnin'", "no more", "a stiff", "bereft of life"]

parrot_list.append("A Norwegnian Blue")
for state in parrot_list:
    print("this parrot is " + state)

even = [2, 4, 6, 8]
odd = [1,3,5,7]
number = even + odd
number.sort()
print(number)

print(number.sort())
# does'nt work as new object formation is not allowed in python
# it will return none

# USE OF BUILT IN FUNCTION SORTED

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
number = even + odd
print(sorted(number))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
number = even + odd
number_in_order = sorted(number)
print(number_in_order)

if number == number_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

if number_in_order == sorted(number):
    print("The lists are equal")
else:
    print("The lists are not equal")

list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal")

print(list("The lists are equal"))

even = [2, 4, 6, 8]

another_even = list(even)
# another_even = sorted(even, reverse=True)
print(another_even is even)
print(another_even == even)

another_even.sort(reverse=True)
print(even)
print(another_even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value,end='\n')