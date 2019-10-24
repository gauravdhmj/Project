import pickle

# imelda = ("more mayhem",
#           "imelda may",
#            2011,
#           ((1,"pulling the rug"),
#            (2,"psycho"),
#            (3,"mayhem"),
#            (4,"kentish town waltz")))
#
# with open("imelda.pickle","wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)
# use of dump command to store the data into the file

# with open("imelda.pickle", "rb") as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
# print(imelda2)
# use of load command to retrieve the data from the pickle file
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
# print(track_list)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)

# ADDING MORE DATA TO THE FILE

imelda = ("more mayhem",
          "imelda may",
           2011,
          ((1,"pulling the rug"),
           (2,"psycho"),
           (3,"mayhem"),
           (4,"kentish town waltz")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998382, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
print(track_list)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print("=" * 40)

for i in even_list:
    print(i)

print("=" * 40)

for i in odd_list:
    print(i)

print("=" * 40)

print(x)

# REMOVE THE PICKLE FILE
# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")     # Windows
# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")     # Mac/Linux

