#Bhurala Code.:):):)
A=[2,3,4,5,7,17,7,9,56,75]               #list 1.
B=[4,2,5,7,11,17,56]              #list 2
C=[]                           #empty list
for i in A:    
    for j in B:
        if i==j:
            C.append(i)        #adding item to new list.
print(C[:])                    #printing items.