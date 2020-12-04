def swap_case(s):
    a = ""
    for i in s:
        if i.isupper():
            a += i.lower()
        elif i.islower():
            a += i.upper()
        else:
            a += i
    return a


s = input()
result = swap_case(s)
print(result)
