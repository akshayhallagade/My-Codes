num=[1,2,3,4,5,6]
while True:
    for i in range(len(num)):
        if i==3:
            del(num[i])
            break
    print(num)        
