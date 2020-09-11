# Question:
"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
"""
# Hints:
"""
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
raw_input = "0100,0011,1010,1001"
raw_input = [number for number in raw_input.split(",")]
empty = []
for raw in raw_input:
    # we have to choose only 4 digit number so "and (len(str(int(raw))) == 4)" was written.
    if (0 == int(raw) % 5) and (len(str(int(raw))) == 4):
        empty.append(int(raw))
print(empty)
