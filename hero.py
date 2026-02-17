import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        ''' 
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        dominator = self.starting_health + opponent.starting_health
        self_win_chance = self.starting_health / dominator

        winner_roll = random.uniform(0, 1)
        if winner_roll < self_win_chance:
            winner = self
        else: 
            winner = opponent

        print(f'{winner.name} Wins!')

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 200)
    hero1.fight(hero2)