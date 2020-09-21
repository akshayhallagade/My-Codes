#This code might find tuff to read so inheritance is used to make it understandable.
class polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[]
        for i in range(no_of_sides):
            self.sides.append(0)
    def input_slides(self):
        for i in range(self.n):
            self.sides[i]=float(input("Enter side "+str(i+1)+":"))
    def  display_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

p1= polygon(3)
p1.input_slides()
p1.display_sides()
