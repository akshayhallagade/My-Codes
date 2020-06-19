#use of pop(),remove(),clear() in the list.

Names=["Ash","Akshay","Likeitaash",1,4,3,5,3.2]

#remove()
Names.remove("Likeitaash") #it is used to remove the item of which we not knew the index number. 
print(Names)

#pop()
Names.pop(1)   #It is generally used when we have to remove the last element if we dont know the. 
print(Names)

#clear()
Names.clear()
print(Names)   #to clear the whole list.
