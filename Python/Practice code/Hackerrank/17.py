import itertools as it
stringg, intt = list(map(str, input().split(" ")))
a = list(it.permutations(stringg, int(intt)))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
aa = []
for i in a:
    print_str = ""
    for j in i:
        print_str += j
    aa.append(print_str)
aa.sort()
for i in aa:
    print(i)
