suminput = int(input("sum: "))
arr = list(map(int, input("arr:").split(" ")))


def productSmallestPair(sum, arr):
    j = arr.pop(arr.index(min(arr)))
    k = arr.pop(arr.index(min(arr)))
    arr1 = arr
    if j == k:
        productSmallestPair(sum, arr1)
    elif j != k and j+k <= sum:
        return j*k


print(productSmallestPair(suminput, arr))
