no_of_pairs = int(input(""))
bride_drink = input("")
groom_drink = input("")
bride_list = list(bride_drink)
groom_list = list(groom_drink)

for i in list(bride_list):
    for j in list(groom_list):
        if i == j:
            bride_list.remove(i)
            groom_list.remove(j)
            no_of_pairs -= 1
            break
    else:
        break
print(no_of_pairs)
