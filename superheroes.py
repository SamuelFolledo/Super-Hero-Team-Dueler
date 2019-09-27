import random

#Ability
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)

class Weapon(Ability):
    def attack(self): #returns a random value from half to full power of the weapon
        return random.randint(self.max_damage // 2, self.max_damage) #floor division (//) divides and returns the integer value of the quoties; dumping digits after the decimal



#Armor
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block 

    def blocks(self):
        return random.randint(0, self.max_block)
    

#Hero
class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_ability(self, ability):
        self.abilities.append(ability)

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

            else:
                print(f"{self.name} has {self.current_health}HP left\n{opponent.name} has {opponent.current_health}HP left")

    def add_kills(self, num_kills):
        self.kills += num_kills


    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    
class Team():
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


##################################################################################################
def test_fight():
    hero1 = Hero("Superman")
    hero2 = Hero("Batman")
    ability1 = Ability("Laser eyes", 30)
    ability2 = Ability("Freeze breath", 10)
    ability3 = Ability("Bat mobile attack", 70)
    ability4 = Ability("Batarang", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

def test_team_methods():
    hero1 = Hero("Superman")
    hero2 = Hero("Batman")
    hero3 = Hero("Spiderman")
    hero4 = Hero("Ryu")
    marvel_team = Team("Marvel")
    marvel_team.add_hero(hero1) 
    marvel_team.add_hero(hero2) 
    marvel_team.add_hero(hero3)
    marvel_team.remove_hero(hero4) 
    marvel_team.remove_hero("Spiderman")  
    marvel_team.view_all_heroes()
    marvel_team.add_hero("Kobe")
    marvel_team.view_all_heroes()
    marvel_team.remove_hero("Batman")
    marvel_team.view_all_heroes()

if __name__ == "__main__":
    test_team_methods()