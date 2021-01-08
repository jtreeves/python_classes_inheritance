class Phone():
    """ Phone class that can used for inheritance; it takes in a phone number and a color as arguments  """
    
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f'phone_number: {self.phone_number}, color: {self.color}'
    
    def call(self, other_number):
        print(f'Calling number: {other_number}')
    
    def text(self, other_number, message):
        print(f'Sending text to {other_number}:')
        print(message)
    
    def open_app(self, app_name):
        print(f'Opening {app_name}')

class Android(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.passcode = None
        self.battery_charge = 50
    
    def __str__(self):
        return f'ANDROID PHONE >> phone_number:{self.phone_number}'
    
    def set_passcode(self, new_passcode):
        self.passcode = new_passcode

    def view_battery_charge(self):
        print(f'Battery Charge: {self.battery_charge}%')
    
    def charge_phone(self, charging_amount):
        self.battery_charge += charging_amount

        if self.battery_charge > 100:
            self.battery_charge = 100

# Don't need () after Phone because it doesn't inherit anything, but you do need them after Android because it inherits Phone