class BMW:
    def fuel_type(self):
        print("BMW uses petrol or diesel.")

    def max_speed(self):
        print("BMW max speed is 250 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses petrol.")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h.")

def car_details(car):
    car.fuel_type()
    car.max_speed()

car1 = BMW()
car2 = Ferrari()

car_details(car1)
print()  
car_details(car2)
