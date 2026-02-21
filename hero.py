import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        abilities: List
        armors: List
        '''
        self.name = name
        self.deaths = 0
        self.kills = 0
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

        
    def add_ability(self, ability):
        ''' 
        Add ability to abilities list
        '''
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        ''' 
        Add weapon to abilities list
        '''
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''
        Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def defend(self):
        '''
        Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    def take_damage(self, attack):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        damage = attack - self.defend()
        damage = max(0, damage)
        self.current_health -= damage
        return f'Attack: {attack} | Damage: {damage}'


    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' 
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        # # Check if Abilities Exist
        # if not self.abilities or not opponent.abilities:
        #     print('Fight cancelled: a hero has unsatisfactory abilities list')
        #     return
        
        # Annouce Battle
        print(f'{self.name} vs {opponent.name}')
        print('------Battle!------')

        # Pick Who Starts
        if random.randint(0, 1) == 0:
            attacker = self
            defender = opponent
        else:
            attacker = opponent
            defender = self

        # Battle
        while self.is_alive() and opponent.is_alive():
            attack = attacker.attack()
            attack_stats = defender.take_damage(attack)

            print(f'{attacker.name} attacks {defender.name}')
            print(attack_stats)
            print(f'{defender.name} health: {defender.current_health}')
            print('------')

            attacker, defender = defender, attacker
        
        # Announce Winner
        if self.is_alive():
            self.add_kill(1)
            opponent.add_death(1)
            print(f'{opponent.name} goes down!')
            print(f'{self.name} wins!')
        else:
            self.add_death(1)
            opponent.add_death(1)
            print(f'{self.name} goes down!')
            print(f'{opponent.name} wins!')


    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    # hero1 = Hero("Wonder Woman", 300)
    # hero2 = Hero("Dumbledore", 200)
    # hero1.fight(hero2)

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Snarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())

    # armor = Armor("The Wall", 100)
    # another_armor = Armor("Brick", 50)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_armor(armor)
    # hero.add_armor(another_armor)
    # print(hero.defend())

    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    # hero1 = Hero("Wonder Woman", 600)
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # ability5 = Ability("Unknown", 300)
    # armor1 = Armor("Bracelets of Submission", 120)
    # armor2 = Armor("Protego", 500)
    # armor3 = Armor("Environment Manipulation", 40)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero2.add_ability(ability5)
    # hero1.add_armor(armor1)
    # hero2.add_armor(armor2)
    # hero2.add_armor(armor3)
    # hero1.fight(hero2)

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())