# perfect #solved #Akhil's problem of TCS
raw_input = int(input())
len_raw_input = len(str(raw_input))
times = str("9"*len_raw_input)
num = 0
n = 0
while int(times) >= n:
    num += 1
    mul = 1
    n += 1
    for i in str(num):
        mul *= int(i)
        if len_raw_input == len(str(mul)) and mul == raw_input:
            print(num)
            quit()
else:
    print("Not Possible")
    quit()
