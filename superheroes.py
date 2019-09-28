import random
########################################## ABILITY CLASS ##########################################
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)

########################################## WEAPON CLASS ##########################################
class Weapon(Ability):
    def attack(self): #returns a random value from half to full power of the weapon
        return random.randint(self.max_damage // 2, self.max_damage) #floor division (//) divides and returns the integer value of the quoties; dumping digits after the decimal

########################################### ARMOR CLASS ##########################################
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block 

    def blocks(self):
        return random.randint(0, self.max_block)

########################################## HERO CLASS##########################################
class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)
        print(f"        Congrats! {self.name} now has a new ability called: {ability.name}")

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        print(f"        Congrats! {self.name} now has a new weapon called: {weapon.name}")

    def add_armor(self, armor):
        self.armors.append(armor)
        print(f"        Congrats! {self.name} now has a new armor called: {armor.name}")

    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.blocks()
        return total_defense

    def take_damage(self, damage):
        damage_to_health = damage - self.defend()
        self.current_health -= damage_to_health

    def is_alive(self):
        return self.current_health > 0 #returns True ifcurrent_health > 0
            
    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
            return
        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
            if self.is_alive() and not opponent.is_alive(): #if self won and not opponent
                print(f"{self.name} won!")
                self.add_kills(1)
                opponent.add_deaths(1)
            elif not self.is_alive() and opponent.is_alive(): #if opponent won
                print(f"{opponent.name} won!")
                self.add_deaths(1)
                opponent.add_kills(1)

    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

########################################## TEAM CLASS ##########################################
class Team:
    def __init__(self, name):
        self.heroes = list()
        self.name = name

    def add_hero(self, hero_name, current_health = 100):
        hero = self.check_hero(hero_name, current_health)
        self.heroes.append(hero)

    def remove_hero(self, hero_name):
        hero = self.check_hero(hero_name)
        if hero in self.heroes: #if we have hero, get index and pop it
            hero_index = self.heroes.index(hero)
            self.heroes.pop(hero_index)
        else:
            return 0

    def view_all_heroes(self):
        if len(self.heroes) > 0:
            print("The heroes are:")
            for hero in self.heroes:
                print(f"- {hero.name}")
            return
        print("We have no heroes to view")

    def check_hero(self, hero, current_health = 100): #BONUS: check hero data type
        if isinstance(hero, str): #if hero is a string, then convert it to a hero class
            temp_hero = Hero(hero, current_health)
            for hero in self.heroes: #search heroes if we have hero exist already
                if hero.name == temp_hero.name:
                    return hero
            return temp_hero #return new Hero class
        return(hero) #if it's already a hero then just return it

    def attack(self, other_team): #pick random players from both teams and make them fight
        hero = random.choice(self.heroes)
        opponent = random.choice(other_team.heroes)
        hero.fight(opponent)

    def revive_heroes(self, current_health=100): #reset heroes's current_health
        for hero in self.heroes:
            hero.current_health = current_health

    def stats(self):
        for hero in self.heroes:
            print(f"- {hero.name} = {hero.kills}/{hero.deaths}")

########################################## ARENA CLASS ##########################################
class Arena:
    def __init__(self):
        self.team_one = Team
        self.team_two = Team

    def create_ability(self):
        ability_name = user_input("     Choose a name for an ability: ")
        ability_max_damage = user_int_input(f"        Damage amount for {ability_name}: ")
        return Ability(ability_name, ability_max_damage)

    def create_weapon(self):
        weapon_name = user_input("      Choose a name for a weapon: ")
        weapon_max_damage = user_int_input(f"         Damage amount for {weapon_name}: ")
        return Weapon(weapon_name, weapon_max_damage)
    
    def create_armor(self):
        armor_name = user_input("       Choose a name for an armor: ")
        armor_max_defense = user_int_input(f"         Block amount for {armor_name}: ")
        return Armor(armor_name, armor_max_defense)

    def create_hero(self, team):
        hero_name = user_input(f"Team {team.name}: Choose a name for the hero#{len(team.heroes) + 1}: ") #added team in the parameter for this, so user won't lose track on which team or player number they're working on
        hero_starting_health = user_int_input(f"Starting health amount for {hero_name}: ")
        hero = Hero(hero_name, hero_starting_health)
        upgrade_types = ["weapon", "ability", "armor"]
        for upgrade_type in upgrade_types:
            user_choice = choice(f"     Would you like to add {a_or_an(upgrade_type)} for {hero.name}? ") #choice is either True of False. a_or_an returns "a weapon" or "an ability"
            while user_choice:
                if upgrade_type == "weapon":
                    hero.add_weapon(self.create_weapon())
                elif upgrade_type == "ability":
                    hero.add_ability(self.create_ability())
                elif upgrade_type == "armor":
                    hero.add_armor(self.create_armor())
                user_choice = choice(f"     Would you like to add another {upgrade_type} for {hero.name}? ")
        return hero

    def build_team_one(self):
        team_one = Team(user_input("Choose a name for Team 1: "))
        team_one_amount = user_int_input(f"   {team_one.name} has how many heroes? ")
        for i in range(team_one_amount):
            hero = self.create_hero(team_one) 
            team_one.add_hero(hero)
        self.team_one = team_one

    def build_team_two(self):
        team_two = Team(user_input("Choose a name for Team 2: "))
        team_two_amount = user_int_input(f"   {team_two.name} has how many heroes? ")
        for i in range(team_two_amount):
            hero = self.create_hero(team_two)
            team_two.add_hero(hero)
        self.team_two = team_two

    def team_battle(self):
        self.team_one.attack(self.team_two)
    
    def show_stats(self):
        print("Team 1:")
        self.team_one.stats()
        print("Team 2:")
        self.team_two.stats()

########################################## Helper Methods ##########################################
def a_or_an(word): #check if first char of a word is a vowel or not
    vowels= ["a", "e", "i", "o", "u"]
    return f"an {word}" if word[0] in vowels else f"a {word}"

def user_input(prompt): #string user input
    user_input = input(prompt) 
    while user_input == "" or any(char.isalnum == False and char.isspace() == False for char in user_input): #accept alphabets, numbers, and white spaces only
        user_input = input("    Error: Please input letters, numbers, and white spaces only: ") #ask for the input again
    return user_input

def choice(prompt): #char user input for y/n
    user_input = input(prompt)
    while user_input != "y" and user_input != "Y" and user_input != "n" and user_input != "N": 
        user_input = input("        Error: Please enter 'y' or 'n' only: ")
    return True if user_input == "y" or user_input == "Y" else False

def user_int_input(prompt): #int user input
    user_input = input(prompt)
    while user_input.isdigit() == False: #ensures the input is an integer
        user_input = input("        Error: Please enter a whole number only: ")
    return int(user_input) 

########################################## MAIN ##########################################
if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()