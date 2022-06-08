import sys


# Start again function.
def start_again():
    start = input("Do you wannna start again? y or n :")
    if start == "y" or "Y":
        main()
    elif start == "n" or "N":
        sys.exit()
    else:
        start_again()


def winner_losser(n1, n2):
    print("...............................................................")
    print("...............................................................")
    print(f".........{n1} is the winner and {n2} is looser ................")
    print("...............................................................")
    print("...............................................................")
    start_again()
# dashboard which board gonna see for game.


def dashboard(n):
    return f" {n[0]} | {n[1]} | {n[2]} \n"+"___________\n"+f" {n[3]} | {n[4]} | {n[5]} \n"+"___________\n"+f" {n[6]} | {n[7]} | {n[8]} "

# winner and looser will be decided with the logic.


def logic(arr, na1, na2):
    if ("X" == arr[0] == arr[1] == arr[2]) or ("X" == arr[3] == arr[4] == arr[5]) or ("X" == arr[6] == arr[7] == arr[8]) or ("X" == arr[0] == arr[3] == arr[6]) or ("X" == arr[1] == arr[4] == arr[7]) or ("X" == arr[2] == arr[5] == arr[8]) or ("X" == arr[0] == arr[4] == arr[8]) or ("X" == arr[2] == arr[4] == arr[6]):
        return winner_losser(na1, na2)
    elif ("O" == arr[0] == arr[1] == arr[2]) or ("O" == arr[3] == arr[4] == arr[5]) or ("O" == arr[6] == arr[7] == arr[8]) or ("O" == arr[0] == arr[3] == arr[6]) or ("O" == arr[1] == arr[4] == arr[7]) or ("O" == arr[2] == arr[5] == arr[8]) or ("O" == arr[0] == arr[4] == arr[8]) or ("O" == arr[2] == arr[4] == arr[6]):
        return winner_losser(na1, na2)
    else:
        pass


def main_list(num=0, enter_value=" ", return_dash=range(10)):
    list_of_dash = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    if num != 0:
        return_dash[num-1] = enter_value
        return return_dash
    else:
        return list_of_dash


def main():
    print("...............................................................")
    print("...............................................................")
    print(".....................Welcome to the Game.......................")
    print("...............................................................")
    print("...............................................................")
    name1 = input(" Enter Your Name (player1): ")
    name2 = input(" Enter Your Name (player2): ")
    print("\n")
    print(f"\t1. {name1}: X is your sign\t", f"2. {name2}: O is your sign\n")
    a = main_list(0, " ")
    print(dashboard(a))
    for i in range(9):
        if i % 2 == 0:
            raw_input1 = int(input(f"{name1} enter position for X :"))
            a = main_list(raw_input1, "X", a)
            print(dashboard(a))
            logic(a, name1, name2)
        elif i % 2 != 0:
            raw_input2 = int(input(f"{name2} enter position for O :"))
            a = main_list(raw_input2, "O", a)
            print(dashboard(a))
            logic(a, name2, name1)
    print("\t........Game is Tied........")
    start_again()


main()
