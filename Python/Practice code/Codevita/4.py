import sys
import math
asl = input()
a = list(asl)
#a = [1,2,3,4,5,10,11,3,6,16]
n = len(a)
su = sum(a)
print(fin(a, n))


def fin(a, n):
    su = 0
    su = sum(a)
    dp = [[0 for i in range(su + 1)]
          for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, su + 1):
        dp[0][j] = False
    for i in range(1, n + 1):
        for j in range(1, su + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]
    diff = sys.maxsize
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break
    ans = int((su/2))+int(diff)
    return ans
