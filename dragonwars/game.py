import rpg_classes

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

#squad list
isaac = Tank("Isaac", club, lightmail)
emilee = Archer("Emilee", magic_wand, dragonmail)
aiden = Engineer("Aiden", sword, chainmail)
meghan = Archer("Meghan", magic_wand, chainmail)
will = Tank("Will", sword, lightmail)