class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
p1=Point(6,8)
print((p1.x, p1.y))

del p1.y # deleting attribute
print(p1.x)
print(p1.y) #this is will show error. due to absence of the y. we had deleted it. 