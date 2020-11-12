# Question£º
"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward
UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current
position after a sequence of movement and original point. If the distance is a float, then just
print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""
# Hints:
"""
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
base_position = [0, 0]
for i in range(4):
    row_input = input().split(" ")
    if row_input[0] == "UP":
        base_position[0] += int(row_input[1])
    elif row_input[0] == "DOWN":
        base_position[0] -= int(row_input[1])
    elif row_input[0] == "LEFT":
        base_position[1] += int(row_input[1])
    elif row_input[0] == "RIGHT":
        base_position[1] -= int(row_input[1])
    else:
        pass
hypo = ((base_position[0]**2)+(base_position[1]**2))**(1/2)
print(f"Then, the output of the program should be:{int(hypo)}")
