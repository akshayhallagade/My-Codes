setA = 16
list_set_A = set(list("1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52".split(" ")))
N = 4
for i in range(N):
    to_do, number = list(map(str, input().split(" ")))
    list_number = list(map(int, input().split(" ")))
    if "intersection_update" in to_do:
        set(list_set_A).intersection_update(set(list_number))
    elif "union" in to_do:
        set(list_set_A).union(set(list_number))
    elif "symmetric_difference" in to_do:
        set(list_set_A).symmetric_difference(set(list_number))
    elif "difference_update" in to_do:
        set(list_set_A).difference_update(set(list_number))
    elif "difference" in to_do:
        set(list_set_A).difference(set(list_number))
    elif "intersection" in to_do:
        set(list_set_A).intersection(set(list_number))
    elif "update" in to_do:
        set(list_set_A).update(set(list_number))
print(sum(list(list_set_A)))
