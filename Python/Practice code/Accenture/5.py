stri = input()
count_dots = stri.count(".")
count_hash = stri.count("-")
count = ""
for i in stri:
    if i == "-":
        continue
    else:
        count += i
print(count_hash*"-", count)
