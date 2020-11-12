no_of_boxes = int(input())
if no_of_boxes % 2 == 0:
    pass
else:
    no_of_boxes += 1

arr = list(map(int, input().split(" ")))
ans = []
addd = []
sum = 0
product = 1
for i in no_of_boxes:
    for j in no_of_boxes:
        for k in no_of_boxes:
            if j > i:
                spl1 = arr[i:j]
                spl2 = arr[i+k:j+k]
                if len(spl1) == len(spl2):
                    spl2.reverse()
                    for p in spl1:
                        for q in spl2:
                            if spl1.index(p) == spl2.index(q):
                                product = p*q
                                sum = sum+product
                                addd.append(sum)
