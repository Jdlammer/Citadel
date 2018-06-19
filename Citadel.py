def welcome():
        print("Hello! Welcome to Citadel.")
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

    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x

    def get_inventory(self):
        return self.inventory

    def get_coordinates(self):
        return self.coordinates



class Enemy:
    def __init__(self,name,description,health, damage):
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage
    def is_alive(self):
        return self.health>0

class Bear(Enemy):
    def __init__(self):
        super().__init__(name="Bear",
                         description="A big brown grizzly",
                         health=200,
                         damage=15)


    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage






welcome()

