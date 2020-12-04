my_dict = {
    "Lions": "Grr",
    "Tigers": "Rawr",
    "Snakes": "Ssss",
    "Birds": "Chirp"
}
noises_hear = list(map(str, input().split(" ")))
for i in noises_hear:
    for (k, v) in my_dict.items():
        if v == i:
            print(k, end=" ")
