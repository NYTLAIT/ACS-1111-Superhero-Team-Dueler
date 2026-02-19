class Animal:
    def __init__(self, name):
        self.name = name

    def is_eating(self):
        print(f'{self.name} is eating')

    def is_drinking(self):
        print(f'{self.name} is drinking')

class Frog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def jump(self):
        print(f'{self.name} is jumping')


# Duck Typing Testing Yay! 
# Need to use has attribute first before callable! This code does not work!
# Will get errors!
def identify(animal):
    if callable(animal.is_eating) and callable(animal.is_drinking):
        print(f'{animal} is an Animal')
        if callable(animal.jump):
            print(f'The {animal} is a Frog')
        else:
            print(f'Type of animal, unknown')

if __name__ == '__main__':
    animal = Animal('Rubert')
    frog = Frog('Ribbit')

    identify(animal)
    identify(frog)

