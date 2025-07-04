class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 
    def __str__(self):
        print("I am inside you")
        return ("{0}, {1}").format(self.x, self.y)
    def __display(self):
        print("Display Method")
    
p1 = Point(2, 3)
print(p1)

p1.__display()