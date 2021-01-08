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
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery_charge = 50
    
    def __str__(self):
        return f'ANDROID PHONE >> phone_number:{self.phone_number}, color:{self.color}, passcode: {self.passcode}, battery_charge:{self.battery_charge}'
    
    def set_passcode(self, new_passcode):
        self.passcode = new_passcode

    def unlock_phone(self, input_passcode):
        if input_passcode == self.passcode:
            print('Phone unlocked')
        else:
            print('Password is incorrect')

    def view_battery_charge(self):
        print(f'Battery Charge: {self.battery_charge}%')
    
    def charge_phone(self, charging_amount):
        self.battery_charge += charging_amount

        if self.battery_charge > 100:
            self.battery_charge = 100

frank_phone = Android('888-777-3333', 'black')
print(f'FRANK_PHONE >> {frank_phone}')
frank_phone.call('456-123-3333')
frank_phone.view_battery_charge()
frank_phone.charge_phone(30)
frank_phone.view_battery_charge()
frank_phone.charge_phone(50)
frank_phone.view_battery_charge()
frank_phone.set_passcode(1234)
print(frank_phone)
frank_phone.unlock_phone(1)
frank_phone.unlock_phone(1234)

# Don't need () after Phone because it doesn't inherit anything, but you do need them after Android because it inherits Phone