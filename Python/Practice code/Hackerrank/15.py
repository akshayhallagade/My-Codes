def print_rangoli(size):
    rever = []
    width = ((2*size)-1)+((2*size)-2)
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    max_printable = alphabets[size-1::-1]  # d,c,b,a
    # max_printable_straight_array = alphabets[:size:]  # a,b,c,d
    for i in range(1, size+1):
        part1 = max_printable[0:i]
        part2 = []
        if i == 1:
            pass
        else:
            part2 = part2 + max_printable[0:i-1]
        adasd = part1+part2[::-1]
        aa = "-".join(adasd)
        bb = aa.center(width, "-")
        rever.append(bb)
        print(bb)

    for i in rever[-2::-1]:
        print(i)


print_rangoli(26)
