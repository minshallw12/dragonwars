class Weapon:
    def __init__(self, name, attack)
        self.name = name
        self.attack = attack
    def get_weapon_name(self):
        return self.name
    def get_weapon_attack(self):
        return self.attack

class Armor:
    def __init__(self, name, defense)
        self.name = name
        self.defense = defense
    def get_weapon_name(self):
        return self.name
    def get_weapon_attack(self):
        return self.attack

#weapons list
club = Weapon("Club", 10)
sword = Weapon("Crossbow", 5)
magic_wand = Weapon("Magic Wand", 15)
#armor list
chainmail = Armor("Chainmail", 10)
lightmail = Armor("Lightmail", 3)
dragonmail = Armor("Dragonmail", 25)


class Tank:
    def __init__(self, name, weapon={}, armor={})
        self.name = name
        self.health = 100
        self.attack = 5
        self.defense = 15
        self.weapon = weapon
        self.armor = armor
        self.deceased = False
    def get_health(self):
        return self.health
    def get_weapon(self):
        return self.weapon
    def set_health(self, new_health):
        self.health = new_health
    def set_weapon(self, old_weapon, new_weapon):
        self.weapon = new_weapon
        self.attack -= old_weapon.get_weapon_attack()
        self.attack += new_weapon.get_weapon_attack()

class Engineer:
    def __init__(self, name, weapon={}, armor={})
        self.name = name
        self.health = 100
        self.attack = 1
        self.defense = 50
        self.weapon = weapon
        self.armor = armor
        self.deceased = False
    def get_health(self):
        return self.health
    def get_weapon(self):
        return self.weapon
    def set_health(self, new_health):
        self.health = new_health
    def set_weapon(self, old_weapon, new_weapon):
        self.weapon = new_weapon
        self.attack -= old_weapon.get_weapon_attack()
        self.attack += new_weapon.get_weapon_attack()

class Archer:
    def __init__(self, name, weapon={}, amror={})
        self.name = name
        self.health = 100
        self.attack = 15
        self.defense = 5
        self.weapon = weapon
        self.armor = armor
        self.deceased = False
    def get_health(self):
        return self.health
    def get_weapon(self):
        return self.weapon
    def get_armor(self):
        return self.armor
    def set_health(self, new_health):
        self.health = new_health
    def set_weapon(self, old_weapon, new_weapon):
        self.weapon = new_weapon
        self.attack -= old_weapon.get_weapon_attack()
        self.attack += new_weapon.get_weapon_attack()
    def set_armor(self, old_armor, new_armor):
        self.armor = new_armor
        self.defense -= old_armor.get_armor_defense()
        self.defense += new_armor.get_armor_defense()



class Team:

    def __init__(self, slot1, slot2={}, slot3={})
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
