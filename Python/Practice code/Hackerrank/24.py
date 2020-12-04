def breakingRecords(scores):
    min_value = 0
    max_value = 0
    list1 = []
    for i in scores:
        if len(list1) == 0:
            pass
        elif i < min(list1):
            min_value += 1
        elif i > max(list1):
            max_value += 1
        list1.append(int(i))
    return max_value, min_value


n = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(breakingRecords(n))
