import os

path = "folders/"
files = os.listdir(path)
for i in range(len(files)):
    source = path + files[i]
    desti = path + str(i+1)
    os.rename(source, desti)

# This code can change the name of the folders and gives the proper number list name to it.
