raw_input = int(input())
len_raw = len(str(raw_input))
raw_out = ""
mul = 1
a = ""
for i in range(1, len_raw+1):
    if a == "cut":
        break
    for j in range(1, 10):
        if a == "cut":
            break
        raw_out += str(j)
        for k in raw_out:
            mul *= int(k)
            if mul == raw_input:
                print(f"{mul}")
                a = "cut"
                break

else:
    print("Not possible")
