from random import randint


class CombatActions:

    def __init__(self, player, enemy):
        # self.character = character
        self.player = player
        self.enemy = enemy

#Private method
    def __diceRoll(self, character):
        print("{}'s turn to roll the dice".format(character))
        roll = randint(1, 6)
        print("{} rolled a {}".format(character, roll))
        return roll

    # def strikeOrder(self):
    #     # global enemy_dice, player_dice
    #     enemy_dice = self.__diceRoll(self.enemy)
    #     player_dice = self.__diceRoll(self.player)
    #
    #     while enemy_dice == player_dice:  # Keep rerolling until there's no tie
    #         print("It's a tie! Rerolling...")
    #         enemy_dice = diceRoll(self.enemy)
    #         player_dice = diceRoll(self.player)
    #
    #     if enemy_dice > player_dice:
    #         print("The enemy was faster and strikes first")
    #         return 'enemy'
    #     else:
    #         print("You were faster and strike first")
    #         return "player"

    def strikeOrder(self):
        print("Rolling the dice...")
        enemy_dice = self.__diceRoll(self.enemy)
        player_dice = self.__diceRoll(self.player)

        while enemy_dice == player_dice:  # reroll ties
            print("It's a tie! Re rolling...")
            enemy_dice = self.__diceRoll(self.enemy)
            player_dice = self.__diceRoll(self.player)

        if enemy_dice > player_dice:
            print("Enemy rolls higher")
            return self.enemy
        else:
            print("You rolled higher")
            return self.player


    def enemyStrike(self, damage, hp):
        print(f"Oh ohh, {self.enemy} is striking you")
        newLife = hp - damage
        return newLife

    def playerStrike(self, damage, hp):
        print(f"What a hit, I am sure that {self.enemy} really felt that one")
        newLife = hp - damage
        return newLife

    def playerTurn(self):
        while True:
            print("What will you do?")
            print("1 - Attack")
            print("2 - Use potion")
            choice = input("--> ")

            if choice == "1":
                return "attack"
            elif choice == "2":
                return "potion"
            else:
                print("Invalid choice — choose again.")