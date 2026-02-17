class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print('dog initialized!')

    def bark(self):
        print('Woof!')

    def roll_over(self):
        print(f'{self.name} rolls over')

    def sit(self):
        print(f'{self.name} sits')
