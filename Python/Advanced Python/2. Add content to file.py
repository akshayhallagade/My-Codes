# write a file.
text = "Ask your pizza delivery guy for a joke, and he'll deliver."
# Creat a file named 2. puns.txt
saveFile = open("2.puns.txt", "w")
saveFile.write(text)
# close file.
saveFile.close()
