# STONE,PAPER,SCISSOR
import sys


def game_starting():
    dots()
    dots()
    dots()
    print(".................Welcome to Game...............")
    dots()
    dots()
    dots()


def dots():
    print("...............................................")


def wrong_input(no_check):
    if int(no_check) < 4:
        pass
    else:
        print("wrong input")
        print("restart game again")
        sys.exit()


def score():
    print(
        "\n\t", name_first_player, ":", points1, "\t", name_second_player, ":", points2,
    )


def winner_declaration():
    if points1 > points2:
        print(".............. Winner is ", name_first_player, "..............")
    else:
        print("..............Winner is ", name_second_player, "..............")


def each_event_result(name):
    print("\n\t[[[ 5 points added to", name, "]]]")


def variables_and_input():
    print("You have to choose from this : \n1. Stone,\n2. Paper,\n3. SCISSOR\n")
    name_first_player = input("Name of First Player : ")  # 1st person
    name_second_player = input("Name of second Player : ")  # 2nd person
    n = 0
    return n, name_first_player, name_second_player


def game_ending():
    dots()
    dots()
    dots()
    winner_declaration()
    dots()
    dots()
    dots()


# MAIN FUNCTION
# Welcome to the game
game_starting()
print("\n\t\tStone, Paper, SCISSOR\n\n\n")

# taking input

n, name_first_player, name_second_player = variables_and_input()

points1 = 0
points2 = 0

while n <= 2:
    n += 1
    print("\n..................round :", n, "...................")
    first_person = input("Enter Input : ")
    wrong_input(first_person)

    # print(name_first_player, ":", first_person)
    Second_person = input("Enter Input : ")
    wrong_input(Second_person)
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
            each_event_result(name_second_player)
            points2 += 5
            score()
            dots()
        elif Second_person == "3":
            print(name_second_player, ": SCISSOR")
            print("\n")
            # result
            print("\t\t STONE vs SCISSOR")
            each_event_result(name_first_player)
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
            each_event_result(name_first_player)
            points1 += 5
            score()
            dots()
        elif Second_person == "3":
            print(name_second_player, ": SCISSOR")
            print("\n")
            # result
            print("\t\t PAPER vs SCISSOR")
            each_event_result(name_second_player)
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
            each_event_result(name_second_player)
            points2 += 5
            score()
            dots()
        elif Second_person == "2":
            print(name_second_player, ": stone")
            print("\n")
            # result
            print("\t\t SCISSOR vs PAPER")
            each_event_result(name_first_player)
            points1 += 5
            score()
            dots()


game_ending()
