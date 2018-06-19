class Player:
    def __init__(self,name=None,attack=None,defense=None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.life = 100
        self.armor = 0
        self.inventory = {
            "Backpack" : [],
            "Map" : []
        }
        self.coordinates = {
            x = 0
            y = 0
        }
class Enemies:
    def __init__(self,type,name,attack=None, defense=None):
        self.name = name
        self.type = type
        self.attack = attack
        self.defense = defense

    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x

    def get_attack(self):
        return self.attack

    def set_attack(self, x):
        self.attack = x

    def get_defense(self):
        return self.defense

    def set_defense(self, x):
        self.defense = x

    def get_inventory(self):
        return self.inventory

    def welcome():
        print("Hello! Welcome to Citadel.")




welcome()

