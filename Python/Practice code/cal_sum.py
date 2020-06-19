def cal_sum(n):
    if n==1:
        return 1
    else:
        if n==10:
            return n
        return n+cal_sum(n+1)
sum=cal_sum(3)
print(sum)
