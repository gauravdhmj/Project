t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imelda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
#
# metallica[0] = "Master of puppets"
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

# A LIST HAS A MUTABLE OBJECT WHILE A TUPLE HAS AN IMMUTABLE OBJECT
#
metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "master of puupets"
print(metallica2)

#
# RIGHT HAND ASSIGNMENT IS EVALUATED FIRST THAN THE LEFT HAND SIDE
a = b = c = d = 12
print(c)
a, b = 12, 13
print(a, b)

a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))
# UNPACKING A TUPLE
metallica2.append("rock")
title, artist, year,n = metallica2
print(title)
print(artist)
print(year)
print(n)

# imelda.append("Jazz")

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)


# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

#
#  A TUPLE CONTAINING A LIST
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))