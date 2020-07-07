# creating a file.
newfile = open("7.puns.txt", "w")
# writing to it.
newfile.write("Akshay")
newfile.close
# appending to it.
newfile = open("7.puns.txt", "a")
newfile.write(" Hallagade")
newfile.close()
# reading to it.
newfile = open("7.puns.txt", "r").read()
print(newfile)
