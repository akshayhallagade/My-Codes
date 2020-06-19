alphas = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
user_input = input("Enter a string : ")  # taking user input
user_input_list = []  # add alphas present in the string.
output = []  # sum of revered  of alphas present and characters.
for i in user_input:
    for j in alphas:
        if i == j:
            user_input_list.append(i)
        else:
            user_input_list.append(" ")
user_input_list = reverse.user_input_list

n1=len(user_input)
n2=len(user_input_list)

while n2>=0:
    output.append
