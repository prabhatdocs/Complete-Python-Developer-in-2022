class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('John', 50, 'gprabhat06@gmail.com')
archer1 = Archer('John', 30)

print(wizard1.email)