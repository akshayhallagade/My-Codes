# 3
# 3 2
# BBB
# RB
# 5 1
# R
# 4 3
# R
# B
# RBRB

# number of test case :
cases = int(input())
answers = []
for n in range(cases):
    # N= max number of string
    # P= number of string input
    n, p = list(map(int, input().split(" ")))
    initials_list = []
    # total outcome
    total_outcome = 2**n
    # 2**4==16

    for i in range(p):
        count = 0
        initial = input()
        # adding inputs to initial list
        initials_list.append(initial)
        len_initial = len(initial)

    # checking if similar items are present
    for j in initials_list:
        for i in initials_list:
            if j == i:
                continue
            elif j in i:
                if len(j) < len(i):
                    initials_list.remove(i)
                # elif j > i:
                #     #
                # elif i in j:
                #     if i < j:
                #         #
                #     elif i > j:
                #         #

    # calling initial_list and making sum of len of all itesm present.
    for j in initials_list:  # 2 items
        # check_in_list(initials_list,j)
        count += (2**(n-len(j)))
        # 2**3==8
        # 2**2==4
        # 4

    answers.append(total_outcome-count)

for i in answers:
    print(i)

# answer = total_outcome - events stating with initials
