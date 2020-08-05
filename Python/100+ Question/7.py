x = 3
y = 5
empty = []
for i in range(x):
    elements = []
    for j in range(y):
        elements.append(i*j)
    empty.append(elements)

print(empty)
