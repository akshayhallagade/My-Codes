#understanding for loop with else.
pro_langu=("Java","Python","C++")
inp_langu=str(input("Enter a name of programming language you know :"))
for i in pro_langu:
    if i==inp_langu:
        print("It is presnet in the list")
        break
else:
    print("your input language is not present here is list.")
