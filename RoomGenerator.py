import random

class generateRoom():
    def __init__(self):
        print("Initialise Room Options")

    def generateEnemy(self, enemyList):
        print("generate enemy")
        enemy = random.choice(enemyList)
        if enemy == "none":
            print("Lucky for you nobody is home")
        else:
            print ("Tough luck buddy, you are gonna have to fight " + enemy)



    def generateLoot(self, loot):
        print("generate loot")
        loot = random.choice(loot)
        print ("Great, you just found a " + loot)

    def choseDungeonSize(self):
        print("Chose how big your adventure should be")
        dungeon = int(input("==>"))
        if(dungeon <= 0):
            print("That's not how this works")
            print("You need to chosoe a number higher than 0")
        elif (dungeon <= 5):
            print("That is a good start.")
            print("You have " + str(dungeon) + " rooms to pass untill safety")
        elif (5 < dungeon <= 10):
            print("Bold choice adventurer.")
            print("You have " + str(dungeon) + " rooms to pass until safety")
        else:
            print("I guess somebody doesn't want to get home today.")
            print("You have " + str(dungeon) + " rooms to pass until safety")
        return dungeon