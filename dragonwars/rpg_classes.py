class Weapon:
    '''Creates a new weapon'''
    def __init__(self, name, attack):
        self._name = name
        self._attack = attack
    def get_name(self):
        return self._name
    def get_attack(self):
        return self._attack

class Armor:
    '''Creates a new armor'''
    def __init__(self, name, defense):
        self._name = name
        self._defense = defense
    def get_name(self):
        return self._name
    def get_defense(self):
        return self._defense

class Item:
    '''Creates a new item'''
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

#-------------------------------------------------------------------------------------------------------------

class CreateClass:
    '''Creates a new character class with differen attributes'''
    def __init__(self, name, health, attack, defense, weapon={}, armor={}):
        self._name = name
        self._health = health
        self._attack = attack
        self._defense = defense
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
        if self.get_weapon() == {}:
            self._weapon = new_weapon
            self._attack += new_weapon.get_attack()
        else:
            self._attack -= self.get_weapon().get_attack()
            self._weapon = new_weapon
            self._attack += new_weapon.get_attack()
    def get_armor(self):
        return self._armor
    def set_armor(self, new_armor):
        if self.get_armor() == {}:
            self._armor = new_armor
            self._defense += new_armor.get_defense()
        else:
            self._defense -= self._armor.get_defense()
            self._armor = new_armor
            self._defense += new_armor.get_defense()

tank = CreateClass("Tank", 120, 10, 15)
engineer = CreateClass("Engineer", 100, 1, 10)
archer = CreateClass("Archer", 100, 7, 2)

#---------------------------------------------------------------------------------------------------------------------------

class Character:
    '''Creates a new character after choosing its class'''
    def __init__(self, name, character_class):
        self._name = name
        self._class = character_class
    def get_name(self):
        return self._name
    def get_class(self):
        return self._class
    #def set_weapon(self, new_weapon)
    
# #squad list
isaac = Character("Isaac", tank)
isaac.get_class().set_weapon(club)
isaac.get_class().set_armor(lightmail)
emilee = Character("Emilee", archer)
emilee.get_class().set_weapon(magic_wand)
emilee.get_class().set_armor(dragonmail)
aiden = Character("Aiden", engineer)
aiden.get_class().set_weapon(club)
aiden.get_class().set_armor(lightmail)
meghan = Character("meghan", archer)
meghan.get_class().set_weapon(magic_wand)
meghan.get_class().set_armor(chainmail)
will = Character("Will", tank)
will.get_class().set_weapon(sword)
will.get_class().set_armor(chainmail)


#------------------------------------------------------------------------------------------------------------------------

class Team:
    def __init__(self, slot1, slot2={}, slot3={}):
        self.slot1 = slot1
        self.slot2 = slot2
        self.slot3 = slot3
    def set_squad(self, slot, new_character):
        if slot == 1:
            self.slot1 = new_character
        if slot == 2:
            self.slot2 = new_character
        if slot == 3:
            self.slot3 = new_character
    def get_slot1(self):
        return self.slot1
    def get_slot2(self):
        return self.slot2 
    def get_slot3(self):
        return self.slot3 


#Teams
team1 = Team(isaac, emilee, aiden)
team1.set_squad(1, meghan)
team2 = Team(will, meghan, isaac)
team3 = Team(aiden, emilee, will)

#------------------------------------------------------------------------------------------------------------------------


print(team1.get_slot1().get_class().get_weapon().get_attack())
print(team2.get_slot2().get_class().get_armor().get_defense())
print(team3.get_slot3().get_class().get_weapon().get_name())
print(team1.get_slot1().get_class().get_armor().get_name())