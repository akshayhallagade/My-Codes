seies_of_square = [7*7, 6*6, 5*5, 4*4, 3*3, 2*2, 1*1]
min_cadbury_l = int(input())
max_cadbury_l = int(input())
min_cadbury_b = int(input())
max_cadbury_b = int(input())

no_student = 0
khali = []
for i in range(min_cadbury_l, max_cadbury_l+1):
    for j in range(min_cadbury_b, max_cadbury_b+1):
        khali.append("{}*{}".format(i, j))
        for k in seies_of_square:
            if i*j >= k:
                (i*j)/k*k
                no_student += 1
                # print(i*j)
print(no_student)
