class Vehicale:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelIX = Vehicale(240, 18)

print("Model Max Speed:", modelIX.max_speed)
print("Model Mileage:", modelIX.mileage)