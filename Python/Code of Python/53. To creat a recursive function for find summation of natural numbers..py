#use of function. #To creat a recursive function. #recursion.
#to find the sum of natural numbers.
def cal_sum(n):
    if n==1:
        return 1
    else:
        return n+cal_sum(n-1)
summ=cal_sum(5)
print(summ)
