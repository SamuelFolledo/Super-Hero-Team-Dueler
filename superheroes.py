import random

#Ability
class Ability:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def attacks(self):
        # damage = random.randint(0, self.attack_strength)
        # print("damage is: ", damage)
        damage = 0
        damage += self.strength
        return damage


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
            total_attack += ability.attacks()
        # print("Total attack is: ",total_attack)
        return total_attack

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.blocks()
        # print("Total Defense is: ",total_defense)
        return total_defense

    def take_damage(self, damage):
        damage_to_health = damage - self.defend()
        # print("Damage to health is: ", damage_to_health)
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

    
    
if __name__ == "__main__":
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