class Dog:
   
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Labrador Retriever")
dog2 = Dog("Max", "German Shepherd")

print("{} is a {}".format(dog1.name, dog1.species))
print("{} is also a {}".format(dog2.name, dog2.species))

print("{} is a {}".format(dog1.name, dog1.breed))
print("{} is a {}".format(dog2.name, dog2.breed))
