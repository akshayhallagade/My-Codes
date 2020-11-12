# Question:
"""
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and 
the values are square of keys. The function should just print the values only.
"""
# Hints:
"""
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
"""


def funct(n1, n2):
    dictt = dict()
    for i in range(n1, n2+1):
        dictt[i] = i**2
    for (k, v) in dictt.items():
        # end=" " it is used to put the curser and at the end of the earlier written value.
        # means, gives output : 1,4,9.... in this way.
        print(v, end=" ")


funct(1, 20)
