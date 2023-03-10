class Weapon:
    def __init__(self, name, attack):
        self._name = name
        self._attack = attack
    def get_name(self):
        return self._name
    def get_attack(self):
        return self._attack

class Armor:
    def __init__(self, name, defense):
        self._name = name
        self._defense = defense
    def get_name(self):
        return self._name
    def get_defense(self):
        return self._attack

class Item:
    def __init__(self, name, value):
        self._name = name
        self._value = value
    def get_item_value(self):
        return self._value

#weapons list
club = Weapon("Club", 10)
sword = Weapon("Sword", 5)
magic_wand = Weapon("Magic Wand", 15)
#armor list
chainmail = Armor("Chainmail", 10)
lightmail = Armor("Lightmail", 3)
dragonmail = Armor("Dragonmail", 25)
#item list
health_potion = Item("Health Potion", 40)
grenade = Item("Grenade", 20)
bread = Item("Bread", 10)


class Tank:
    def __init__(self, name, weapon={}, armor={}):
        self._name = name
        self._health = 100
        self._attack = 10
        self._defense = 15
        self._weapon = weapon
        self._armor = armor
        self._inventory = {}
        self._deceased = False
    def get_health(self):
        return self._health
    def get_weapon(self):
        return self._weapon
    def set_health(self, new_health):
        self._health = new_health
    def set_weapon(self, new_weapon):
        self._attack -= self.get_weapon().get_attack()
        self._weapon = new_weapon
        self._attack += new_weapon.get_attack()
    def get_armor(self):
        return self._armor
    def set_armor(self, new_armor):
        self._defense -= self._armor.get_defense()
        self._armor = new_armor
        self._defense += new_armor.get_defense()

class Engineer:
    def __init__(self, name, weapon={}, armor={}):
        self._name = name
        self._health = 100
        self._attack = 1
        self._defense = 10
        self._weapon = weapon
        self._armor = armor
        self._inventory = {}
        self._deceased = False
    def get_health(self):
        return self._health
    def get_weapon(self):
        return self._weapon
    def set_health(self, new_health):
        self._health = new_health
    def set_weapon(self, old_weapon, new_weapon):
        self._weapon = new_weapon
        self._attack -= old_weapon.get_attack()
        self._attack += new_weapon.get_attack()
    def get_armor(self):
        return self._armor
    def set_armor(self, new_armor):
        self._defense -= self._armor.get_defense()
        self._armor = new_armor
        self._defense += new_armor.get_defense()

class Archer:
    def __init__(self, name, weapon={}, armor={}):
        self._name = name
        self._health = 100
        self._attack = 7
        self._defense = 2
        self._weapon = weapon
        self._armor = armor
        self._inventory = {}
        self._deceased = False
    def get_health(self):
        return self._health
    def get_weapon(self):
        return self._weapon
    def set_health(self, new_health):
        self._health = new_health
    def set_weapon(self, old_weapon, new_weapon):
        self._weapon = new_weapon
        self._attack -= old_weapon.get_attack()
        self._attack += new_weapon.get_attack()
    def get_armor(self):
        return self._armor
    def set_armor(self, new_armor):
        self._defense -= self._armor.get_defense()
        self._armor = new_armor
        self._defense += new_armor.get_defense()

#squad list
isaac = Tank("Isaac", club, lightmail)
emilee = Archer("Emilee", magic_wand, dragonmail)
aiden = Engineer("Aiden", sword, chainmail)
meghan = Archer("Meghan", magic_wand, chainmail)
will = Tank("Will", sword, lightmail)

class Team:
    def __init__(self, slot1, slot2={}, slot3={}):
        self.slot1 = slot1
        self.slot2 = slot2
        self.slot3 = slot3
    def set_squad(self, slot, new_character):
        if slot == "1":
            self.slot1 = new_character
        if slot == "2":
            self.slot2 = new_character
        if slot == "3":
            self.slot3 = new_character
    def get_squad_slot1(self):
        return self.slot1
    def get_squad_slot2(self):
        return self.slot2 
    def get_squad_slot3(self):
        return self.slot3 


#Teams
team1 = Team(isaac, emilee, aiden)
team2 = Team(will, meghan, isaac)
team3 = Team(aiden, emilee, will)

print(team1.get_squad_slot1().get_weapon().get_name())
print(meghan.get_weapon().get_name())
print(team2.get_squad_slot2().get_armor().get_name())
print(team3.get_squad_slot3().get_weapon().get_attack())