class Car():
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def start(self):
        print("The Car is starting.......")

Car1 = Car("Honda Civic","black")
Car1.start()
