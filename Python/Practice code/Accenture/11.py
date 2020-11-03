n = int(input("Enter the size of array : "))
empty = []
even = []
odd = []
for i in range(n):
    empty.append(int(input(f"enter element at {i} index : ")))

for i in range(1, len(empty)+1):
    if i % 2 == 0:
        odd.append(empty[i-1])
    else:
        even.append(empty[i-1])
print("Sorted even array : ", sorted(even))
print("Sorted odd array : ", sorted(odd))
