class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
p1=Point(6,8)
print((p1.x, p1.y))

del p1 #Deleted object p1
print(p1) #It will show error.