def checking(N, n_space):
    if N == len(n_space):
        pass
    else:
        print("error")


T = int(input("number of testcases."))
total_gifts = []
for i in range(T):
    N = int(input("number of employees."))
    N_space = input("N space separating interger.")
    n_space = list(N_space.split(" "))
    checking(N, n_space)
    total = []
    for j in n_space:
        if len(n_space) == 1:
            total.append(1)
        elif n_space.index(j) == 0:
            if n_space[0] == n_space[1]:
                total.append(1)
                if len(total) == len(n_space):
                    break
            elif n_space[0] != n_space[1]:
                total.append(1)
                # total.append(2)
                if len(total) == len(n_space):
                    break
        elif len(total) == len(n_space):
            break
        elif int(j) == n_space[len(n_space)-1]:
            if n_space[len(n_space)-2] == n_space[len(n_space)-1]:
                if total[len(total)-1 == 1]:
                    total.append(1)
                    if len(total) == len(n_space):
                        break
                elif total[len(total)-1 == 2]:
                    total.append(2)
                    if len(total) == len(n_space):
                        break
            elif n_space[len(n_space)-2] != n_space[len(n_space)-1]:
                if total[len(total)-1 == 1]:
                    total.append(1)
                    if len(total) == len(n_space):
                        break
                elif total[len(total)-1 == 2]:
                    total.append(2)
                    if len(total) == len(n_space):
                        break
        elif j == n_space[n_space.index(j)-1]:
            if total[len(total)-1] == 1:
                total.append(1)
                if len(total) == len(n_space):
                    break
            else:
                total.append(2)
                if len(total) == len(n_space):
                    break
        elif j != n_space[n_space.index(j)-1]:
            if total[len(total)-1] == 1:
                total.append(2)
                if len(total) == len(n_space):
                    break
            else:
                total.append(1)
                if len(total) == len(n_space):
                    break
    total_gifts.append(sum(total))
print(total_gifts)
for m in total_gifts:
    print(m)
