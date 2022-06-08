# STONE,PAPER,SCISSOR
import sys
import random


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


# def wrong_input(no_check):
#     if int(no_check) < 4:
#         pass
#     else:
#         print("wrong input")
#         print("restart game again")
#         sys.exit()


def score():
    print(
        "\n\t", name_first_player, ":", points1, "\t", name_second_player, ":", points2,
    )


def winner_declaration():
    if points1 > points2:
        print(".............. Winner is ", name_first_player, "..............")
    elif points1 == points2:
        print("......... OHhooo, No win No Loose..............")
    else:
        print("..............Winner is ", name_second_player, "..............")


def each_event_result(name):
    print("\n\t[[[ 5 points added to", name, "]]]")


def game_ending():
    dots()
    dots()
    dots()
    winner_declaration()
    dots()
    dots()
    dots()


# ............................... MAIN FUNCTION .....................................
# Welcome to the game
game_starting()
print("\n\t\tStone, Paper, SCISSOR\n\n\n")

# NAME OF THE PLAYER
print("You have to choose from this : \n1. Stone,\n2. Paper,\n3. SCISSOR\n")
name_first_player = input("Name of First Player : ")  # 1st person
# name_second_player = input("Name of second Player : ")  # 2nd person
name_second_player = "Pikachu"
print("Hello,", name_first_player,
      " I am Pikachu. I am player along uh.  Lets start.")
print("Pika Pika.")
n = 0

points1 = 0
points2 = 0
A = [1, 2, 3]

while n <= 2:
    n += 1
    print("\n..................round :", n, "...................")

    # FIRST INPUT
    while True:
        first_person = int(input("Enter Input : "))
        if first_person in [1, 2, 3]:
            break
        else:
            pass

    # SECOND INPUT
    Second_person = random.choice(A)
    print("Pikachu Input : ", Second_person)
    print("\n")

    # CODE LOGIC (Having all conditions)
    if first_person == Second_person:
        print("\t", name_first_player, name_second_player, "both are same")
        print("\t\t [[[Tied]]]")
        score()
        dots()
    elif first_person == 1:
        print(name_first_player, ": Stone")
        if Second_person == 2:
            print(name_second_player, ": Paper")
            print("\n")
            # result
            print("\t\t STONE vs PAPER")
            each_event_result(name_second_player)
            points2 += 5
            score()
            dots()
        elif Second_person == 3:
            print(name_second_player, ": SCISSOR")
            print("\n")
            # result
            print("\t\t STONE vs SCISSOR")
            each_event_result(name_first_player)
            points1 += 5
            score()
            dots()
    elif first_person == 2:
        print(name_first_player, ": Paper")
        if Second_person == 1:
            print(name_second_player, ": Stone")
            print("\n")
            # result
            print("\t\t PAPER vs STONE")
            each_event_result(name_first_player)
            points1 += 5
            score()
            dots()
        elif Second_person == 3:
            print(name_second_player, ": SCISSOR")
            print("\n")
            # result
            print("\t\t PAPER vs SCISSOR")
            each_event_result(name_second_player)
            points2 += 5
            score()
            dots()
    elif first_person == 3:
        print(name_first_player, ": SCISSOR")
        if Second_person == 1:
            print(name_second_player, ": Stone")
            print("\n")
            # result
            print("\t\t SCISSOR vs STONE")
            each_event_result(name_second_player)
            points2 += 5
            score()
            dots()
        elif Second_person == 2:
            print(name_second_player, ": stone")
            print("\n")
            # result
            print("\t\t SCISSOR vs PAPER")
            each_event_result(name_first_player)
            points1 += 5
            score()
            dots()

# GAME ENDING
game_ending()
