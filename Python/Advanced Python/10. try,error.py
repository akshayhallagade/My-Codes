import os
try:
    filename = "10. Presidency.txt"
    f = open(filename, 'r').read()
    print(f)

except IOError:
    print("problem reading : ", filename)
