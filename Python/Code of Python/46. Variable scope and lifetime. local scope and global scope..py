#variable scope and lifetime. #local scope and global scope.
def my_love():
    x=10                                       #local scope
    print("This is the value inside :",x)

x=20
my_love()                                      #global scope.
print("Value outside the function",x)          