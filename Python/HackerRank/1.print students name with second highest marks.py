if __name__ == '__main__':
    list1 = []
    marks = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])
        if score in marks:
            pass
        else:
            marks.append(score)
    while maxx in marks:
        maxx = max(marks)
    maxx2 = max(marks)
    name = []
    for i in range(len(list1)):
        if maxx2 == list1[i][1]:
            name.append(list[i][0])
    for i in name:
        print(i)
