
s = "123"
last = []
final = []
for i in range(len(s)):
    if s[i].isalnum:
        final.append(True)
    else:
        final.append(False)
last.append(True if True in final else False)
final = []
for i in range(len(s)):
    if s[i].isalpha:
        final.append(True)
    else:
        final.append(False)
last.append(True if True in final else False)
final = []
for i in range(len(s)):
    if s[i].isdigit:
        final.append(True)
    else:
        final.append(False)
last.append(True if True in final else False)
final = []
for i in range(len(s)):
    if s[i].islower:
        final.append(True)
    else:
        final.append(False)
last.append(True if True in final else False)
final = []
for i in range(len(s)):
    if s[i].isupper:
        final.append(True)
    else:
        final.append(False)
last.append(True if True in final else False)
for j in last:
    print(j)
