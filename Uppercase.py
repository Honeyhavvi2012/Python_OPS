class IOString():

    def __init__(self):
        self.str = ""

    def get_String(self):
        self.str1 = input("Enter String:")

    def print_String(self):
        print("Result is :", self.str1.upper())

str = IOString()

str.get_String()
str.print_String()