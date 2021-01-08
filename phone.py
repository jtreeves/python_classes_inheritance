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
    def __init__(self, phone_number, color, size):
        super().__init__(phone_number, color)
        self.size = size
        self.passcode = None
        self.battery_charge = 50
    
    def __str__(self):
        return f'ANDROID PHONE >> phone_number:{self.phone_number}, color:{self.color}, size: {self.size}, passcode: {self.passcode}, battery_charge:{self.battery_charge}'
    
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

class Galaxy(Android):
    def __init__(self, phone_number, color, size, fold):
        super().__init__(phone_number, color, size)
        self.fold = fold
    
    def __str__(self):
        return f'GALAXY PHONE >> phone_number:{self.phone_number}, color:{self.color}, size: {self.size}, fold: {self.fold}'
    
    def fold_phone(self):
        self.fold = True
    
    def unfold_phone(self):
        self.fold = False
    
    def check_fold_status(self):
        if self.fold:
            print('Your phone is folded.')
        else:
            print('Your phone is unfolded.')

galaxy_z_phone = Galaxy('123-456-7890', 'blue', 'big', False)
print(f'GALAXY_Z_PHONE >> {galaxy_z_phone}')
galaxy_z_phone.call('456-123-0987')
galaxy_z_phone.view_battery_charge()
galaxy_z_phone.fold_phone()
galaxy_z_phone.check_fold_status()
galaxy_z_phone.unfold_phone()
galaxy_z_phone.check_fold_status()

frank_phone = Android('888-777-3333', 'black', 'small')
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