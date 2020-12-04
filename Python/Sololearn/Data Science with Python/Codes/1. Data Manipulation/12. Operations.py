import re
raw_input = input()
x = re.findall("watch?v=", raw_input)
a, b, c, d = map(str, input().split("/"))
if x in raw_input:
    print(x)
else:
    print(d)
