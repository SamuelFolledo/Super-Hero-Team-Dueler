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
        block = random.randint(0, self.max_block)
        print("block is: ", block)
        return block
    

#Hero
class Hero:
    def __init__(self, name, current_health = 100):
        self.name = name
        self.current_health = current_health
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
        return self.current_health > 0 #returns True if health > 0
            
    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                if self.is_alive() and not opponent.is_alive(): #if self won and not opponent
                    print(f"{self.name} won!")
                elif not self.is_alive() and opponent.is_alive(): #if opponent won
                    print(f"{opponent.name} won!")
                else:
                    print(f"{self.name} has {self.current_health}HP left\n{opponent.name} has {opponent.current_health}HP left")

    
class Team():
    def __init__(self, name):
        self.heroes = list()
        self.name = name

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero_name):
        hero_names_list = list()
        for hero in self.heroes:
            hero_names_list.append(hero.name)
        if hero_name in hero_names_list: #if we have hero, get index and pop
            hero_index = hero_names_list.index(hero_name)
            self.heroes.pop(hero_index)
        else:
            return 0

    def view_all_heroes(self):
        print("The heroes are:")
        if len(self.heroes) > 0:
            for hero in self.heroes:
                print(f"\n- {hero.name}")
        else:
            print("We have no heroes to view")

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



if __name__ == "__main__":
    hero1 = Hero("Superman")
    hero2 = Hero("Batman")
    hero3 = Hero("Spiderman")
    hero4 = Hero("Ryu")
    marvel_team = Team("Marvel")
    marvel_team.add_hero(hero1) 
    marvel_team.add_hero(hero2) 
    marvel_team.add_hero(hero3)
    marvel_team.view_all_heroes() 
    marvel_team.remove_hero(hero4) 
    marvel_team.remove_hero("Spiderman")  
    # marvel_team.add_hero("kobe")

    marvel_team.view_all_heroes()