str1 = input("str:")
p1 = input("ch1 :")
p2 = input("ch2 :")


def ReplaceCharacter(str1, ch1, ch2):
    empty = ""
    for i in str1:
        if i == ch1 or i == ch2:
            empty += compare(i, ch1, ch2)
        else:
            empty += i
    return empty


def compare(a, ch, ph):
    if a == ch:
        return ph
    elif a == ph:
        return ch


print(ReplaceCharacter(str1, p1, p2))
