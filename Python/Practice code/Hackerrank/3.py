primes = [199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109, 107,
          103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
empty = []
raw_input = int(input())
for i in primes:
    empty1 = 0
    while raw_input % i == 0:
        raw_input = raw_input/i
        if empty1 == 0:
            empty1 = i
        else:
            empty1 += i
        empty.append(empty1)
empty.sort()
a = ""

for i in empty:
    if i in empty:
        a += str(i)
print(int(a))
print()
