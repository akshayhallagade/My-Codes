def findsum(arr):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[(len(arr)-1)-i][i]
    if sum1 > sum2:
        return sum1-sum2
    elif sum2 > sum1:
        return sum2-sum1
    else:
        return 0


print(findsum([[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]]))
