from random import randint

from generators.ItemGenerator import ItemGenerator
from generators.PlayerGenerator import PlayerGenerator
# from choiceDemo import Choice
from generators.EnemyGenerator import EnemyGenerator
# from generators.EnemyStats import enemies_stats
from actions.Actions import Actions
from generators.roomGenerator import generateRoom
from generators.InventoryGenerator import Inventory
from actions.MoveActions import *
from generators.texts import *
from items import *
from actions.InventoryInteractions import *
import os

#create a room

"""
Goals:
Create Castle gate room
Find key to castle gate
add key to inventory
use key to open the a
"""

# startRoom = generateRoom("Start", "This is the start of the journey", ["forward"])
# castleGame = generateRoom("Castle Gate", "The entrance to the derelict castle", ["forward","back"])

inventory  = Inventory()


playerIsAlive = True
gameIsOn = True

def stopGame():
    global gameIsOn
    gameIsOn = False
    print("GameOver")


def clear_screen():
    """Clears the console screen for a fresh UI experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

# print(castleGame)
# print(castleGame.showExists())

# playerName = input("What's your name? ")
playerName = "John the Player"
print(welcome_text)
print("hello "+ playerName)

# to do
# get the stats of the items from the inventory



# items generation, adding to inventory and ussage
gemStone = ItemGenerator(gem_dict)
print(inventory)
addItemToInventory(inventory,gemStone)
print(inventory.getInventoryItemStats(gemStone))
# removeItemFromInventory(inventory,gemStone)

print(inventory)
print("Use items =============================")
print(inventory.useItem(gemStone))
print("Use items =============================")
print(inventory)


# main game v2 bellow VVVVVV

def forestScene():
    # global playerIsAlive, inventory, gameIsOn
#     Create room for forest scene
    forest = generateRoom("Forest", forestSceneDescription,["GateHouse", "Leave"],forestSceneOptions)

    # Show Room Description
    print(forest.description)
    print()
    print(inventory)
    print()
    # print(forest.options)

    choices = [
        (1, "Go in the gatehouse", gateHouseScene),  # If choice is 1, go to nextSceneTest
        (2, "Leave", stopGame)  # If choice is 2, end the game
    ]

    makeChoice(choices)
# TODO add resolution to choices
def gateHouseScene():
    global playerIsAlive, inventory, gameIsOn

    # gateHouse = generateRoom("GateHouse", "Gatehouse Description", ["Inside", "Forest"])
    #
    # print(gateHouse.description)

    choices = [
        (1, "There is no way you could open the gate like that", gateHouseScene),  # If choice is 1, go to nextSceneTest
        (2, "You try to squeeze through the crack but a boulder shits and the whole pylon crashes onto you and kills you", stopGame),
        (3, "You manage to force open the door",gateHouseRoom)# If choice is 2, end the game
    ]

    makeChoice(choices)

def gateHouseRoom():
    print("Gatehouse room $$$$$$$$$$$$$$$$$")



while playerIsAlive and gameIsOn:
    forestScene()





