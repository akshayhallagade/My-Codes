# Question:
"""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated 
numbers. Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""
# Hints:
"""
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
raw_input = "1,2,3,4,5,6,7,8,9"
raw_input = list(raw_input.split(","))
result = []
for i in raw_input:
    if int(i) % 2 != 0:
        result.append(int(i))
print(result)
