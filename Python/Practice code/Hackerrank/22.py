def sockMerchant(n, ar):
    SetOfArr = set(ar)  # {3,4,5,5,6,7}
    counting_pair = dict()
    for i in SetOfArr:
        counting_pair[i] = ar.count(i)//2
    return sum(counting_pair.values())


n = 7
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))
