# Question:
"""
Please write a program which count and print the numbers of each character in a string input by console.
"""
# Example:
"""
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""
# Hints:
"""
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.
"""
raw_input = "abcdefgabc"
dict1 = dict()
for i in raw_input:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
for j in dict1:
    print(f"{str(j)},{dict1.get(j)}")
