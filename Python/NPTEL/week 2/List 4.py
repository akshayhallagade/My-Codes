strsample = "learning is fun"
print(strsample)
# to capitalize the 1st aplhabet of the strsample.
print(strsample.capitalize())
# to capitalize 1st alphabet of each word. (to write it as a TITLE.)
print(strsample.title())
# to swaping the case.
print(strsample.swapcase())
# to find the index of the given letter.
print(strsample.find("n"))
# to count the number of times the letter is used.
print(strsample.count("a"))
# to replace the word with another word.
print(strsample.replace("fun", "yeah"))
# to return yes, if all are follows in the list..
print(strsample.isalnum())  # True, if all are num.
print(strsample.isalpha())  # True, if all are string.
strsample1 = "23234234"
print(strsample1.isdigit())  # True, if all charachters are digit in string.

name1 = "Akshay"
name2 = "Aniket"
name3 = "Saurabh"
print(f"names are :{name1},{name2},{name3}")  # method 1        # both are same
print("names are :{},{},{}".format(name1, name2, name3))  # method 2
