# Question:
"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
# Hints:
"""
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
empty_words = []
empty_number = []
raw_input = "hello world! 123"
for raw in raw_input:
    if raw.isdigit():
        empty_number.append(raw)
    elif raw.isalpha():
        empty_words.append(raw)
print("LETTERS :", len(empty_words), "\nDIGITS :", len(empty_number))
