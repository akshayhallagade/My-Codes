def samllestnumber(num):
    if num < 10:
        print(num+10)
        pass
    ans_list = []
    for i in range(9, 1, -1):
        while num % i == 0:
            num = num / i
            ans_list.append(i)
    if num > 10:
        print("Not Possible")
        pass

    num = ans_list[len(ans_list)-1]
    for j in range(len(ans_list)-2, -1, -1):
        num = (10 * num) + ans_list[j]
    return num


samllestnumber(56)
