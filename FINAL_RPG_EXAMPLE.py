import random
import sys
import time


class Monster:
    #Method in a class receives the instance as the first argument automatically.
    #This is the constructor, it is a function that is automatically called
    #when an instance of the class (an object) is created.
    def __init__(self, name, lvl, hp, crit_chance, attk_1, attk_2, attk_3):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.crit_chance = crit_chance
        self.attk_1 = attk_1
        self.attk_2 = attk_2
        self.attk_3 = attk_3

    #Prints out monster's name and HP.
    def monster_info(self):
        return '{} {}'.format(self.name, self.hp)

class Player:
    def __init__(self, lvl, hp, crit_chance, attk_1, attk_2, attk_3):
        self.lvl = lvl
        self.hp = hp
        self.crit_chance = crit_chance
        self.attk_1 = attk_1
        self.attk_2 = attk_2
        self.attk_3 = attk_3


def battle_1(player, monster):
    print("Satan approaches. Prepare yourself!")
    monster_crit = (monster.attk_1 * 2)
    you_crit = (player.attk_1 * 2)
    while player.hp > 0 and monster.hp > 0:
        crit = random.randint(0, 100)
        if crit in range(0, monster.crit_chance):
            player.hp -= monster_crit
            print(monster.name, " got a critical strike!")
            time.sleep(2)
            print(monster.name, " attacked you for ", monster_crit, " damage.")
            time.sleep(2)
            if player.hp <= 0:
                print("You have been slain.")
                time.sleep(2)
                sys.exit()
            else:
                print("You have ", player.hp, " remaining.\n")
                time.sleep(2)
        else:
            player.hp -= monster.attk_1
            print(monster.name, " attacked you for ", monster.attk_1, " damage.")
            time.sleep(2)
            if player.hp <= 0:
                print("You have been slain.")
                time.sleep(2)
                sys.exit()
            else:
                print("You have ", player.hp, " remaining.\n")
                time.sleep(2)
        print("You can (1) basic attack for 4 damage or (2) stand there.")
        choice = input()
        while choice != "1" and choice != "2":
            choice = input("(1) or (2)? ")
        if choice == "1":
            crit = random.randint(0,100)
            if crit in range(0, player.crit_chance):
                monster.hp -= you_crit
                print("You landed a critical strike!")
                print("You attacked ", monster.name, " for ", you_crit, " damage.")
                if monster.hp <= 0:
                    print("You have slain the foul ", monster.name, "!")
                    time.sleep(2)
                    sys.exit()
                else:
                    print(monster.name, " has ", monster.hp, " remaining.")
                    
            else:
                monster.hp -= player.attk_1
                print("You attacked ", monster.name, " for ", player.attk_1, " damage.")
                if monster.hp <= 0:
                    print("You have slain the foul ", monster.name, "!")
                    time.sleep(2)
                    sys.exit()
                else:
                    print(monster.name, " has ", monster.hp, " remaining.")
                

jimmie = Player(1, 100, 3, 4, 0, 0)
satan = Monster("Satan", 100, 100, 10, 5, 7, 0)

print(Monster.monster_info(satan))

battle_1(jimmie, satan)
