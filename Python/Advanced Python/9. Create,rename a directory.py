import os
# printing directory path.
curDir = os.getcwd()
print(curDir)

# creating new folder.
os.mkdir("newDir")
# renaming it.
os.rename("newDir", "9.newDir2")
