# j = open("C:\\Users\\mukes\\OneDrive\\Desktop\\fileio.txt","r")
# for i in j:
#     if "JABBERWOCK" in i.upper():
#         print(i,end="")
# j.close()
#
# jabber = open("fileio.txt",'r')
# jabber = open("C:\\Users\\mukes\\OneDrive\\Desktop\\fileio.txt","r")
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')

# jabber.close()

# use of with command
# no need to close the file

# with open("fileio.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# READLINE- reads one line at a time

# with open("fileio.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# converting the text into list
# Readlines - Read whole paragraph or all the lines

# with open("fileio.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)

# for line in lines:
#     print(line, end='')

# DIFFERENCE BETWEEN READLIMES AND READ COMMAND

with open("fileio.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')


with open("fileio.txt", 'r') as jabber:
    lines = jabber.read()
#
for line in lines[::-1]:
    print(line, end='')
