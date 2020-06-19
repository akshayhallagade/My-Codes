while True:
    houses=int(input())
    if houses==3:
        print()
    elif houses>=3:
        perc=int(200//houses)
        if perc==int(perc):
            print(perc)
        else:
            print(int(perc+1))
    else:
        print("wrongs input")