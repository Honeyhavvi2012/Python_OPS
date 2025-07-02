class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

r = float(input("Radius: "))

c = Circle(r)

print("Area:", c.area())
print("Perimeter:", c.perimeter())
