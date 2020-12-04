def merge_the_tools(string, k):
    final = []
    string = list(string)
    while len(string) > 0:
        addd = ""
        strr = string[:k]  # splitting.
        for i in range(k):
            string.pop(0)
        strr = list(dict.fromkeys(strr))  # removing duplicates.
        for i in strr:
            addd += i  # addding whole one by one to alphabets.
        final.append(addd)  # adding whole words.

    for i in final:
        print(i)


string, k = input(), int(input())
merge_the_tools(string, k)
