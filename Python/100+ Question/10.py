# Question:
"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""
# Hints:
"""
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""
# 1
row_input = "hello world and practice makes perfect and hello world again"
row_input = list(row_input.split(" "))
row_input = list(set(row_input))
row_input = sorted(row_input)
print(row_input)
# 2
row_input = "hello world and practice makes perfect and hello world again"
row_input = [words for words in row_input.split(" ")]
row_input = sorted(list(set(row_input)))
print(row_input)
