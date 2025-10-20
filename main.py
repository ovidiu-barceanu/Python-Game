from random import randint

from numpy.f2py.rules import options
from actions.CombatActions import CombatActions
from generators.EnemyGenerator import EnemyGenerator
from generators.EnemyStats import enemies_stats
from generators.PlayerGenerator import PlayerGenerator
from generators.InventoryGenerator import Inventory, ItemNotFoundError
from generators.texts import *
from items import *
from actions.InventoryInteractions import *
import os

# Steps:
# Initialise room generator
# Initialize inventory generator
# Use room options
# Use inventory





playerIsAlive = True
gameIsOn = True

def stopGame():
    global gameIsOn
    gameIsOn = False
    print("Game Stopped")

def GameOver():
    global gameIsOn
    gameIsOn = False
    print("GameOver")

def pause():
    input("Press Enter to continue... ")

# TODO this function doesn't work. error : TERM environment variable not set.
def clear_screen():
    """Clears the console screen for a fresh UI experience."""
    os.system('cls' if os.name == 'nt' else 'clear')


print(welcome_text)
pause()
print("===========")

playerName = input("--> What's your name: ")
player = PlayerGenerator(playerName, 10, 1)

print()
# printTarty1("hello   "+ player.name)
print(f"Hello {playerName}. Get ready for your adventure")

pause()
print("===========")


#Initialize inventory
backpack = Inventory()


def scene01():

    print("this is first scene")


#Generate item

    healthPotion = ItemGenerator(health_potion_dict)
    print("Strolling down the forest path towards your village you find a health potion")
    print("Do you want to pick it up?")

    while True:
        print("1 - yes")
        print("2 - no")
        choice = input("--> ")

        if choice == "1":
            backpack.add_item(healthPotion)
            break
        elif choice == "2":
            print("You decided not to pick up the health potion")
            break
        else:
            print("Invalid choice — choose again.")


    pause()
    print("===========")

    print("Continuing your stroll towards your village something jumps in front of you")
    pause()

    #fight scene
#Create enemy
    goblin = EnemyGenerator(*enemies_stats["Goblin"])

# Display enemy stats
    print(f"Oh no, looks like a {goblin.enemyType} decided to attack you")
    print()
    print(f"Enemy HP is {goblin.hp}")
    print(f"Enemy type is {goblin.enemyType}")
    print(f"Enemy damage is {goblin.damage}")

    pause()
    print("=========")
    print()

    fight01=CombatActions(player, goblin)

    print("Let's see who starts the attack")
    print()
    order = fight01.strikeOrder()
    pause()
    print("=========")
    print()

    if order == player:
        print("Keeping your temper you decide to act first,ask questions later")
        print(f"You land the first strike on the nasty {goblin.enemyType}")
        goblin.hp = fight01.playerStrike(player.playerDamage, goblin.hp)

    else:
        print(f"Oh no, the {goblin.enemyType} took you by surprise and lands the first strike")
        player.playerHp = fight01.enemyStrike(goblin.damage, player.playerHp)

    pause()
    print("=========")



    while player.playerHp > 0 and goblin.hp > 0:

        print(f"Goblin HP: {goblin.hp}")
        print(f"{player.name}'s HP: {player.playerHp}")
        print("-" * 30)
        pause()  # optional: wait for user input between turns
        print("===========")

        #Player's turn

        while True:
            action = fight01.playerTurn()

            if action == "attack":
                goblin.hp = fight01.playerStrike(player.playerDamage, goblin.hp)
                break

            elif action == "potion":

                try:
                    potion = backpack.getItemByType("Health Potion")
                    backpack.useItem(potion)
                    player.playerHp += 2
                    break
                except ItemNotFoundError as e:
                    print(e)
            else:
                print("Invalid action. Try again")



        #Check if enemy is defeated
        if goblin.hp <= 0:
            print(f"You defeated {goblin.enemyType}")
            scene02()
            return



        #Enemy's turn
        print(f"{goblin.enemyType} is attacking")
        player.playerHp = fight01.enemyStrike(goblin.damage, player.playerHp)

        if player.playerHp <= 0:
            print("You have been defeated...")
            GameOver()


def scene02():
    print("Second scene to be implemented")
    print("press enter to stop the game")
    pause()
    stopGame()
while playerIsAlive and gameIsOn:
    scene01()


