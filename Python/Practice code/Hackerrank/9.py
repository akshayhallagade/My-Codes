a = int(input("Enter the number : "))
ans = []
if a > 1:
    for i in range(2, a):
        if a % i == 0:
            for j in range(1, 10):
                for k in range(1, 10):
                    temp = j*k
                    if temp == a:
                        ans.append(f"{j}{k}")
            print(ans[0])
            break
    else:
        print("Not Possible")
