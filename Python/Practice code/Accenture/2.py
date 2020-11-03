length = int(input())
arr = []
arr = list(map(int, input().split(" ")))

arr_even = []
arr_odd = []
if len(arr) <= 3:
    print(0)

for i in range(length):
    if i % 2 == 0:
        arr_odd.append(arr[i])
    elif i % 2 != 0:
        arr_even.append(arr[i])
arr_odd.remove(max(arr_odd))
arr_even.remove(max(arr_even))
print(max(arr_even) + max(arr_odd))
