a = b = True
while a == True:
    x = input('\nEnter two to five numbers separated by commas: ').split(',')
    if x.index(0) == True:
        print('\n No zeroes.')
    if len(x) < 2:
        while b == True:
            x.append(input('\nTwo numbers are needed. Enter one more: '))
            b = False
    if len(x) > 5:
        print('\nDon\'t enter more than five numbers.')
        continue
    a = False
