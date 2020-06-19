points_scored = int(input())
cost_of_squirt = int(input())
ticket = points_scored // 12
if ticket > cost_of_squirt:
    print("Buy it")
else:
    print("Try again")
