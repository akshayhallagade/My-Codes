import random as rd
list1 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]
list1 = list1[::-1]
summ = 100
split1 = list1[0:5]
split2 = list1[5:]
if sum(split1) != 100:
    remain = sum(split1)-summ
    print(remain)
