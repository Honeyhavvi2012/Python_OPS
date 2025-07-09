class Reverse:
    def __init__(self, s=""):
        if s == "":
            self.s = input("Enter a word: ")
        else:
            self.s = s

    def get_reversed(self):
        return self.s[::-1]

r = Reverse()  
print("Reversed string:", r.get_reversed())
