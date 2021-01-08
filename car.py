class Car():
    """ Car class that will display the make, model, and color """
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.gas = 10
    
    def __str__(self):
        return 'make: {}, model: {}, color: {}'.format(self.make, self.model, self.color)

    def drive(self):
        self.gas -= 1
    
    def fill_tank(self):
        self.gas = 10
    
    def check_gas(self):
        print(f'You have {self.gas} gallons of gas in the tank.')

car1 = Car('Toyota', 'Corolla', 'silver')

print(car1)
car1.drive()
car1.drive()
car1.fill_tank()
car1.drive()
car1.check_gas()