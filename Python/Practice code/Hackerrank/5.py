raw_input = int(input())
out = ""
for i in range(1, 10):
    remi = ""
    for j in range(1, 10):
        if i*j == raw_input:
            print(out:=f"{i}{j}")
            remi = "cut"
            break
    if remi == "cut":
        break
if out == "":
    print("Not possible")
