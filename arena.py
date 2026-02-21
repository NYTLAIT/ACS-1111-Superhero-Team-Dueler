from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''
        Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = None
        self.team_two = None
        self.current_winner = {"team": None, "champions": None}

    def create_ability(self):
        '''
        Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name?    ")
        max_damage = input("What is the max damage of the ability?    ")
        return Ability(name, max_damage)
    
    def create_weapon(self):
        '''
        Prompt user for Weapon information
        return Weapon with values from user input.
        '''
        name = input("What is the weapon name?    ")
        max_damage = input("What is the max damage of the weapon?    ")
        return Weapon(name, max_damage)
    
    def create_armor(self):
        '''
        Prompt user for Armor information
        return Armor with values from user input.
        '''
        name = input("What is the armor name?    ")
        max_block = input("What is the max block of the armor?    ")
        return Armor(name, max_block)
    
    def create_hero(self):
        '''
        Prompt user for Hero information
        return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero_health = input("Hero's health: ")
        hero = Hero(hero_name, hero_health)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero
    
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_one_name = input("What is the name of Team One?    ")
        self.team_one = Team(team_one_name)

        numOfTeamMembers = int(input("How many members would you like on Team One?    "))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_two_name = input("What is the name of Team Two?    ")
        self.team_two = Team(team_two_name)

        numOfTeamMembers = int(input("How many members would you like on Team Two?    "))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        print('---------------------------')
        print(f'- {self.team_one.name} VS {self.team_two.name} -')
        print('---LET THE BATTLE BEGIN!---')

        winning_team, living_champions = self.team_one.attack(self.team_two)
        self.current_winner["team"] = winning_team
        self.current_winner["champions"] = living_champions

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # Team member stats
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # K/D for Team One
        team_one_kills = 0
        team_one_deaths = 0
        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths
        if team_one_deaths == 0:
            team_one_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_one_kills/team_one_deaths))

        # K/D for Team Two
        team_two_kills = 0
        team_two_deaths = 0
        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        if team_two_deaths == 0:
            team_two_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_two_kills/team_two_deaths))

        # Heroes from Team Two that survived
        for hero in self.current_winner["champions"]:
                print("survived from " + self.current_winner["team"] + ": " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
