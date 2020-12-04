def staircase(n):
    for i in range(n-1, -1, -1):
        for j in range(n+1):
            if i+j == n:
                print((i*" ")+("#"*j))


staircase(6)
