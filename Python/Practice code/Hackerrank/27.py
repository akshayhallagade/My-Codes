n = int(input())
length = []
binary = str(bin(n).replace("0b", "")).split("0")
for i in binary:
    length.append(len(i))
print(max(length))
