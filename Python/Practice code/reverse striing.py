user = input("Enter a string : ")
user_list = list(user)
alphas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
          "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
chara = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<",
         ">", "?", ";", ":", "~,", "/", "|", "*", "-", "+"]
empty = []
index_list_chara = []
final_list = []
for x in user:
    for y in chara:
        if x == y:
            b = user_list.index(x)
            index_list_chara.append(b)

for i in alphas:
    for k in user:
        if i == k:
            empty.append(i)
