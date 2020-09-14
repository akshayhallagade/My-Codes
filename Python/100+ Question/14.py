# Question:
"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""
# Hints:
"""
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
upper_case = []
lower_case = []
raw_input = "Hello world!"
for i in raw_input:
    if i.isupper():
        upper_case.append(i)
    elif i.islower():
        lower_case.append(i)
print("UPPER CASE :", len(upper_case), "\nLOWER CASE :", len(lower_case))
