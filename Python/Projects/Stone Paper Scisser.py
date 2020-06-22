# STONE,PAPER,SCISSOR


def dots():
    print("...............................................")


def score():
    print(
        "\n\t", name_first_player, ":", points1, "\t", name_second_player, ":", points2,
    )


def winner_declaration():
    if points1 > points2:
        print(".............. Winner is ", name_first_player, "..............")
    else:
        print("..............Winner is ", name_second_player, "..............")


# Welcome to the game
dots()
dots()
dots()
print(".................Welcome to Game...............")
dots()
dots()
dots()
print("\n\t\tStone, Paper, SCISSOR\n\n\n")

# taking first input (1st Person)
print("You have to choose from this : \n1. Stone,\n2. Paper,\n3. SCISSOR\n")
name_first_player = input("Name of First Player : ")
name_second_player = input("Name of second Player : ")
n = 0
points1 = 0
points2 = 0

while n <= 2:
    n += 1
    print("\n..................round :", n, "...................")
    first_person = input("Enter Input : ")
    # print(name_first_player, ":", first_person)
    Second_person = input("Enter Input : ")
    print("\n")
    # print(name_second_player, ":", Second_person)

    if first_person == Second_person:
        print("\t", name_first_player, name_second_player, "both are same")
        print("\t\t [[[Tied]]]")
        score()
        dots()
    elif first_person == "1":
        print(name_first_player, ": Stone")
        if Second_person == "2":
            print(name_second_player, ": Paper")
            print("\n")
            # result
            print("\t\t STONE vs PAPER")
            print("\n\t\t[[[", name_second_player, "Won ]]]")
            points2 += 5
            score()
            dots()
        elif Second_person == "3":
            print(name_second_player, ": SCISSOR")
            print("\n")
            # result
            print("\t\t STONE vs SCISSOR")
            print("\n\t\t[[[", name_first_player, "Won ]]]")
            points1 += 5
            score()
            dots()
    elif first_person == "2":
        print(name_first_player, ": Paper")
        if Second_person == "1":
            print(name_second_player, ": Stone")
            print("\n")
            # result
            print("\t\t PAPER vs STONE")
            print("\n\t\t[[[", name_first_player, "Won ]]]")
            points1 += 5
            score()
            dots()
        elif Second_person == "3":
            print(name_second_player, ": SCISSOR")
            print("\n")
            # result
            print("\t\t PAPER vs SCISSOR")
            print("\n\t\t[[[", name_second_player, "Won ]]]")
            points2 += 5
            score()
            dots()
    elif first_person == "3":
        print(name_first_player, ": SCISSOR")
        if Second_person == "1":
            print(name_second_player, ": Stone")
            print("\n")
            # result
            print("\t\t SCISSOR vs STONE")
            print("\n\t\t[[[", name_second_player, "Won ]]]")
            points2 += 5
            score()
            dots()
        elif Second_person == "2":
            print(name_second_player, ": stone")
            print("\n")
            # result
            print("\t\t SCISSOR vs PAPER")
            print("\n\t\t[[[", name_first_player, "Won ]]]")
            points1 += 5
            score()
            dots()
dots()
dots()
dots()
winner_declaration()
dots()
dots()
dots()
