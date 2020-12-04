set1 = set(list(map(int, input().split())))
list1 = []
for i in range(int(input())):
    set2 = set(list(map(int, input().split())))
    if set1.issuperset(set2) and len(set1) > len(set2):
        list1.append(True)
    else:
        list1.append(False)
if False in list1:
    print(False)
else:
    print(True)
