class User():
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self, name, power):
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

wizard1 = Wizard('John', 50)
archer1 = Archer('John', 100)
# wizard1.attack()
# archer1.attack()

print(isinstance(wizard1, object))
print(isinstance(archer1, User))