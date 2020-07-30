khali = input("")
num = input("")
num = list(num.split(" "))
total_pairs = []
for i in num:
    largest = int(max(list(str(i))))
    smallest = int(min(list(str(i))))

    bit_score = str((largest*11)+(smallest*7))
    if len(bit_score) == 2:
        total_pairs.append(bit_score)
        print(bit_score)
    else:
        total_pairs.append(bit_score[1]+bit_score[2])
        print(bit_score[1]+bit_score[2])
no_of_pairs = 0
print(total_pairs)
for j in range(0, len(total_pairs) % 2 == 0 or len(total_pairs) % 2 == 1):
    for k in range(len(total_pairs) % 2 == 0 or len(total_pairs) % 2 == 1, 0):
        if j == k:
            no_of_pairs += 1
            total_pairs.remove(j)
            total_pairs.remove(j)
for l in range(0, len(total_pairs), 2):
    # if l % 2 == 1:
    del total_pairs[l]
print(len(total_pairs)+no_of_pairs)
